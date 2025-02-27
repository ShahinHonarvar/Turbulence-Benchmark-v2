from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    if len(s) < 57:
        return list(result)
    for i in range(len(s) - 56):
        for perm in permutations(s[i:i + 57]):
            if ''.join(perm) not in result:
                result.add(''.join(perm))
    return list(result)