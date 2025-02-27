from itertools import permutations

def palindromes_between_indices(s):
    s = s.lower()
    possible_chars = ''.join([c for c in s[:6] if c.isalpha()])
    palindromes = set()
    for p in set(permutations(possible_chars, len(possible_chars))):
        candidate = ''.join(p)
        if candidate == candidate[::-1] and len(candidate) >= 6:
            palindromes.add(candidate)
    return palindromes