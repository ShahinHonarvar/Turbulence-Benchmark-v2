from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    if len(s) < 106:
        return []
    for i in range(len(s) - 105):
        for perm in permutations(s[i:i + 106]):
            if ''.join(perm) not in result:
                result.add(''.join(perm))
    return list(result)