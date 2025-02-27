from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 8:
        return set()
    substr = s[5:8].lower()
    letters = [c for c in substr if c.isalpha()]
    result = set()
    for length in range(3, len(letters) + 1):
        for perm in permutations(letters, length):
            if perm == perm[::-1]:
                result.add(''.join(perm))
    return result