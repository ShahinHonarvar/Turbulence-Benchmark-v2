import itertools

def palindromes_between_indices(s):
    s = s[1:9].lower()
    letters = [c for c in s if c.isalpha()]
    result = set()
    for r in range(6, len(letters) + 1):
        for p in itertools.permutations(letters, r):
            w = ''.join(p)
            if w == w[::-1]:
                result.add(w)
    return result