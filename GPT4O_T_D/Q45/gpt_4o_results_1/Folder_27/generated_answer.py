from itertools import permutations

def palindromes_between_indices(s):
    substring = s[2:9].lower()
    letters = [ch for ch in substring if ch.isalpha()]
    result = set()
    for perm in permutations(letters, 6):
        half = perm[:3]
        if tuple(reversed(half)) == perm[3:]:
            result.add(''.join(perm))
    return result