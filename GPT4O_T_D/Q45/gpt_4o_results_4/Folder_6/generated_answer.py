from itertools import permutations

def palindromes_between_indices(s):
    substr = s[:8].lower()
    letters = [char for char in substr if char.isalpha()]
    if len(letters) < 4:
        return set()
    result = set()
    for i in range(4, len(letters) + 1):
        for perm in set(permutations(letters, i)):
            candidate = ''.join(perm)
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result