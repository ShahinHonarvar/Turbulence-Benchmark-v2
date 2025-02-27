from itertools import permutations

def palindromes_between_indices(s):
    substring = s[:7]
    letters = [c.lower() for c in substring if c.isalpha()]
    results = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            if perm == perm[::-1]:
                results.add(''.join(perm))
    return results