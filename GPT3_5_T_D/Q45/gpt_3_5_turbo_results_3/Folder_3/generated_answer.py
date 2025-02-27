import itertools
    from string import ascii_letters

def palindromes_between_indices(string):
    letters = [c.lower() for c in string[7:10] if c.isalpha()]
    perms = set((''.join(perm) for perm in itertools.permutations(letters)))
    palindromes = [perm for perm in perms if len(perm) >= 3 and perm == perm[::-1]]
    return set(palindromes)