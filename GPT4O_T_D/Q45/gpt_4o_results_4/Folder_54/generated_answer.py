from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    substring = s[4:10].lower()
    letters = [ch for ch in substring if ch.isalpha()]
    result_set = set()
    for perm in permutations(letters):
        for length in range(4, len(perm) + 1):
            for start in range(len(perm) - length + 1):
                candidate = perm[start:start + length]
                if candidate == candidate[::-1]:
                    result_set.add(''.join(candidate))
    return result_set