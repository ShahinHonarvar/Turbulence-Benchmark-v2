from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 5:
        return set()
    substr = s[3:5].lower()
    letters = [char for char in substr if char.isalpha()]
    if len(letters) < 3:
        return set()
    result = set()
    for perm in set(permutations(letters, len(letters))):
        for length in range(3, len(perm) + 1):
            for subset in set(permutations(perm, length)):
                candidate = ''.join(subset)
                if candidate == candidate[::-1]:
                    result.add(candidate)
    return result