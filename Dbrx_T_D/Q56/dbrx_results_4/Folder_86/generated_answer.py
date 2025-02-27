from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for char in s:
        if len(s) < 143:
            return []
        if len(result) == 143:
            break
        for perm in permutations(s):
            if len(''.join(perm)) == 143 and ''.join(perm) not in result:
                result.add(''.join(perm))
    return list(result)