from itertools import permutations

def palindromes_between_indices(s):
    substring = s[8:10].lower()
    palindromes = set()
    for r in range(3, len(substring) + 1):
        perms = permutations(substring, r)
        for perm in perms:
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes