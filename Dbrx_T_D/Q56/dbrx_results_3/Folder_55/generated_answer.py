from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    if len(s) < 40:
        return []
    for i in range(len(s) - 39):
        for perm in permutations(s[i:i + 40]):
            if len(''.join(set(perm))) == 40:
                result.add(''.join(perm))
    return list(result)