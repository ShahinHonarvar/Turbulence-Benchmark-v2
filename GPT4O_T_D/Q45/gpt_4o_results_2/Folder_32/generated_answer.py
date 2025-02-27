from itertools import permutations

def palindromes_between_indices(s):
    s = s[1:8]
    valid_chars = [c.lower() for c in s if c.isalpha()]
    results = set()
    if len(valid_chars) < 5:
        return results
    for length in range(5, len(valid_chars) + 1):
        for perm in permutations(valid_chars, length):
            if ''.join(perm) == ''.join(perm)[::-1]:
                results.add(''.join(perm))
    return results