from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:7].lower()
    palindromes = set()
    for i in range(4, len(substring) + 1):
        perms = set(permutations(substring, i))
        for perm in perms:
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes