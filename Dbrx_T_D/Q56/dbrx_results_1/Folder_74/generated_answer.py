from collections import defaultdict
from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for n in range(1, min(len(s), 98)):
        for perm in permutations(s, n):
            if ''.join(perm) not in result:
                result.add(''.join(perm))
    return list(result)