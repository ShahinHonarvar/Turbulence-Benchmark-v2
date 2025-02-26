from itertools import permutations

def palindromes_between_indices(s):
    letters = ''.join(filter(str.isalpha, s[3:8])).lower()
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for perm in permutations(letters, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes