import itertools

def palindromes_between_indices(s):
    chars = [c.lower() for c in s[4:9] if c.isalpha()]
    result = set()
    for r in range(4, len(chars) + 1):
        for p in itertools.permutations(chars, r):
            if p == p[::-1]:
                result.add(''.join(p))
    return result