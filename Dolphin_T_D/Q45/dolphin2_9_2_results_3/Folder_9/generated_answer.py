from itertools import permutations

def palindromes_between_indices(s):
    s = ''.join(filter(str.isalpha, s))[:7]
    s = s.lower()
    letters = set(s)
    result = set()
    for p in permutations(letters, len(s)):
        p = ''.join(p)
        if p == p[::-1] and len(p) >= 7:
            result.add(p)
    return result