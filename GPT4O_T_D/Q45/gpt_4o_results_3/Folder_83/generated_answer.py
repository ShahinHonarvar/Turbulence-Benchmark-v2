from itertools import permutations

def palindromes_between_indices(s):
    if not s or len(s) < 10:
        return set()
    substring = s[2:10]
    letters = [char.lower() for char in substring if char.isalpha()]
    result = set()
    for p in permutations(letters):
        candidate = ''.join(p)
        if len(candidate) >= 7 and candidate == candidate[::-1]:
            result.add(candidate)
    return result