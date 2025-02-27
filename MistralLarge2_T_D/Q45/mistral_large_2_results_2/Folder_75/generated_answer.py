from itertools import permutations

def palindromes_between_indices(s):
    chars = ''.join(filter(str.isalpha, s[2:5])).lower()
    palindromes = set()
    for length in range(3, len(chars) + 1):
        for perm in permutations(chars, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes