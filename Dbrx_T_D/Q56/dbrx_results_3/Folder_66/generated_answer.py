from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    for p in permutations(s, 26):
        sub = ''.join(p)
        if len(sub) == len(set(sub)):
            result.append(sub)
    return list(set(result))