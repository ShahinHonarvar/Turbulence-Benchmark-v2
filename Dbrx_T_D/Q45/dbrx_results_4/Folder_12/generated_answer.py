from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[3:9] if c.isalpha()]
    perms = [''.join(p) for i in range(4, len(letters) + 1) for p in permutations(letters, i)]
    palindromes = {perm for perm in perms if perm == perm[::-1]}
    return palindromes