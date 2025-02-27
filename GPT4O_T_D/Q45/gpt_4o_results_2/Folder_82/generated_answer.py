from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:7].lower()
    chars = [c for c in s if c.isalpha()]
    palindromes = set()
    for perm in permutations(chars):
        for mid_char in chars:
            candidate = ''.join(perm) + mid_char + ''.join(reversed(perm))
            if candidate == candidate[::-1] and len(candidate) >= 7:
                palindromes.add(candidate)
    return palindromes