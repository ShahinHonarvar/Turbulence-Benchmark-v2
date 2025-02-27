from itertools import permutations

def palindromes_between_indices(s):
    letters = [c for c in s[2:9] if c.isalpha() and c.isascii()]
    if len(letters) < 3:
        return set()
    half = ''.join(sorted(set((c.lower() for c in letters))))
    result = set()
    for r in range(3, len(half) + 1):
        for p in permutations(half, r):
            palindrome = ''.join(p) + ''.join(p[::-1])
            result.add(palindrome)
    return result