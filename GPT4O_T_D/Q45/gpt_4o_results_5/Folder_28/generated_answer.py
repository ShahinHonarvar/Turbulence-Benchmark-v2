from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 6:
        return set()
    substr = ''.join([char.lower() for char in s[1:6] if char.isalpha()])
    results = set()
    if len(substr) >= 4:
        for i in range(4, len(substr) + 1):
            for perm in permutations(substr, i):
                candidate = ''.join(perm)
                if candidate == candidate[::-1]:
                    results.add(candidate)
    return results