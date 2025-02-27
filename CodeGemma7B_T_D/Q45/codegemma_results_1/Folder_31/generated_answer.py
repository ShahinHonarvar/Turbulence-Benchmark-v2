from itertools import permutations
    from string import ascii_lowercase

def palindromes_between_indices(s):
    result = set()
    for perm in permutations(s, r=8):
        p = ''.join(perm)
        if p.startswith(p[::-1]) and (p >= '0' and p <= '9' or p in ascii_lowercase) and p.lower().endswith(p[:4:-1]):
            result.add(p)
    return result