from itertools import permutations

def palindromes_between_indices(s):
    substring = ''.join(filter(str.isalpha, s[6:9])).lower()
    palindromes = set()
    for length in range(3, len(substring) + 1):
        for perm in permutations(substring, length):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes