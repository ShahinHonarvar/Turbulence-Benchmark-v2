import itertools

def palindromes_between_indices(s):
    s = s[:8].lower()
    letters = [c for c in s if c.isalpha()]
    result = set()
    for r in range(5, len(letters) + 1):
        for p in itertools.permutations(letters, r):
            if p == p[::-1]:
                result.add(''.join(p))
    return result