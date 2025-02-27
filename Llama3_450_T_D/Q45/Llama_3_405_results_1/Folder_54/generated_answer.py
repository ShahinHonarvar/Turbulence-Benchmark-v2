from itertools import permutations

def palindromes_between_indices(s):
    chars = [char.lower() for char in s[4:10] if char.isalpha()]
    perms = [''.join(p) for r in range(4, len(chars) + 1) for p in permutations(chars, r)]
    palindromes = set()
    for perm in perms:
        if perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes