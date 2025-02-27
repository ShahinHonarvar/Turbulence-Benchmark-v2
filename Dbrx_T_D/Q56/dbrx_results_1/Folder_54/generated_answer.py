from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 27):
        for perm in permutations(s[i:i + 28]):
            if len(''.join(set(perm))) == 28:
                result.add(''.join(perm))
    return list(result)