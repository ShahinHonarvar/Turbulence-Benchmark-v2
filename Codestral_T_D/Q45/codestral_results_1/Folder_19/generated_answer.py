from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    substring = s[1:8]
    perms = set(permutations(substring))
    palindromes = set()
    for perm in perms:
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 7:
            palindromes.add(word)
    return palindromes