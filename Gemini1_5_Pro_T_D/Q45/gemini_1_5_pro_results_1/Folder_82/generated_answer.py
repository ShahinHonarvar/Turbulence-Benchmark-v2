from itertools import permutations

def palindromes_between_indices(text):
    result = set()
    s = ''.join(sorted((c for c in text[1:7] if c.isalpha()))).lower()
    for l in range(7, len(s) + 1):
        for p in permutations(s, l):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result