from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(98, len(s) + 1):
        for perm in permutations(s[i - 98:i]):
            if ''.join(perm) not in result:
                result.add(''.join(perm))
    return list(result)