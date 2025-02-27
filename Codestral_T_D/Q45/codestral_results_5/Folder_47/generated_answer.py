from itertools import permutations

def palindromes_between_indices(s):
    letters = s[3:8]
    letters = letters.lower()
    perms = set(permutations(letters, r=None))
    palindromes = set()
    for perm in perms:
        word = ''.join(perm)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    return palindromes