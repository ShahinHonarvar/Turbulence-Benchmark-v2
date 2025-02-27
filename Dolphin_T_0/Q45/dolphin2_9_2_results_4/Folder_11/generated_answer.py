from itertools import permutations

def palindromes_between_indices(s):
    palindromes = set()
    substring = ''.join(filter(str.isalpha, s[3:8]))
    for p in range(4, len(substring) + 1):
        for perm in permutations(substring, p):
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word.lower())
    return palindromes