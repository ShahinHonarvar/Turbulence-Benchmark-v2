from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for n in range(len(s)):
        for perm in permutations(s, n + 1):
            if len(''.join(perm)) == 74 and len(''.join(perm)) == len(set(''.join(perm))):
                result.add(''.join(perm))
    return list(result)