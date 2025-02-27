from itertools import permutations

def palindromes_between_indices(s):
    s = s[2:9].lower()
    letters_only = [c for c in s if c.isalpha()]
    results = set()
    for p in permutations(letters_only):
        candidate = ''.join(p)
        if len(candidate) >= 6 and candidate == candidate[::-1]:
            results.add(candidate)
    return results