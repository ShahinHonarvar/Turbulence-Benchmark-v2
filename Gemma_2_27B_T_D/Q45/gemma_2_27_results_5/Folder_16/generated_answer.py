from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(text[6:10])
    result = set()
    for perm in permutations(letters):
        candidate = ''.join(perm).lower()
        if candidate == candidate[::-1] and len(candidate) >= 5:
            result.add(candidate)
    return result