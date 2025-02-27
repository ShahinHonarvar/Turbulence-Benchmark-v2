from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    subsequence = s[5:10].lower()
    letters_in_range = [char for char in subsequence if char.isalpha()]
    if len(letters_in_range) < 6:
        return set()
    result = set()
    for perm in set(permutations(letters_in_range, 6)):
        candidate = ''.join(perm)
        if candidate == candidate[::-1]:
            result.add(candidate)
    return result