import itertools

def palindromes_between_indices(s):
    English_chars = [c.lower() for c in s[3:9] if c.isalpha()]
    pals = set()
    for r in range(4, len(English_chars) + 1):
        for perm in itertools.permutations(English_chars, r):
            p = ''.join(perm)
            if p == p[::-1]:
                pals.add(p)
    return pals