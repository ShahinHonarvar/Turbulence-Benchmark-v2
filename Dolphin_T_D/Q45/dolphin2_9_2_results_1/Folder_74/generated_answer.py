from itertools import permutations
    import string

def palindromes_between_indices(s):
    pals = set()
    substring = ''.join((c for c in s if c.lower() in string.ascii_lowercase))
    if len(substring) < 6:
        return pals
    for p in permutations(substring, len(substring)):
        for i in range(len(p) - 5):
            for j in range(i + 5, len(p) + 1):
                sub = ''.join(p[i:j])
                if sub == sub[::-1] and len(sub) >= 6:
                    pals.add(sub)
    return pals