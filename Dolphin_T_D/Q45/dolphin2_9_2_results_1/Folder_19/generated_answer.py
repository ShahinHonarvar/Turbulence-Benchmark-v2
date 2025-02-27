import itertools

def palindromes_between_indices(s):
    substring = s[1:8]
    perms = set((''.join(p) for i in range(7, 0, -1) for p in itertools.permutations(substring, i)))
    palindromes = [p.lower() for p in perms if p.lower() == p.lower()[::-1] and len(p.lower()) >= 7]
    return set(palindromes)