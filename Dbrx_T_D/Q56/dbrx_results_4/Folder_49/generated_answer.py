from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 72):
        for perm in permutations(s[i:i + 73]):
            if ''.join(perm) not in result:
                result.add(''.join(perm))
    return list(result)