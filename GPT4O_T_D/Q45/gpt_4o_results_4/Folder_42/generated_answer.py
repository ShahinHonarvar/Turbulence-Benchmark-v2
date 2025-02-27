from itertools import permutations

def palindromes_between_indices(s):
    if len(s) < 10:
        return set()
    sub_str = ''.join(filter(str.isalpha, s[6:10])).lower()
    if len(sub_str) < 3:
        return set()
    results = set()
    for length in range(3, len(sub_str) + 1):
        for perm in set(permutations(sub_str, length)):
            if ''.join(perm) == ''.join(perm)[::-1]:
                results.add(''.join(perm))
    return results