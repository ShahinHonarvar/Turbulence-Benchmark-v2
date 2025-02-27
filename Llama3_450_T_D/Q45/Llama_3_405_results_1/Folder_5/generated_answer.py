import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[4:9] if c.isalpha() and c.lower() in 'abcdefghijklmnopqrstuvwxyz']
    perms = set()
    for r in range(4, len(letters) + 1):
        for perm in itertools.permutations(letters, r):
            perms.add(''.join(perm))
    palindromes = set()
    for perm in perms:
        if perm == perm[::-1]:
            palindromes.add(perm)
    return palindromes