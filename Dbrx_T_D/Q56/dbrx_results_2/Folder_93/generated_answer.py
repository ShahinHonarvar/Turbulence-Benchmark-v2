from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    for p in permutations(s, 54):
        substring = ''.join(p)
        if len(substring) == len(set(substring)):
            result.append(substring)
    return list(set(result))