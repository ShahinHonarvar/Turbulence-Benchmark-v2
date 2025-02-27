from itertools import permutations

def palindromes_between_indices(s):
    substring = s[3:6].lower()
    perms = set(permutations(substring))
    palindromes = set()
    for perm in perms:
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 4:
            palindromes.add(word)
    return palindromes