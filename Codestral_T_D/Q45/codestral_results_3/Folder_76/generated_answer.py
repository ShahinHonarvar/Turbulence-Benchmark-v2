from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    substring = s[1:5]
    palindromes = set()
    perms = permutations(substring)
    for perm in perms:
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes