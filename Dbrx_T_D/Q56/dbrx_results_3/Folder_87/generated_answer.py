from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for p in permutations(s, 58):
        substring = ''.join(p)
        if len(substring) == len(set(substring)):
            result.add(substring)
    return list(result)