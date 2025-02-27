from itertools import permutations

def palindromes_between_indices(s):
    s = s[3:7].lower()
    palindromes = set()
    for i in range(3, len(s) + 1):
        perms = set(permutations(s, i))
        for perm in perms:
            word = ''.join(perm)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes