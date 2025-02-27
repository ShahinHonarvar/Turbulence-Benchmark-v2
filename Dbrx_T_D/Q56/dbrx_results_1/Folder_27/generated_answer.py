from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for p in permutations(s, 57):
        sub = ''.join(p)
        if len(sub) == len(set(sub)):
            result.add(sub)
    return list(result)