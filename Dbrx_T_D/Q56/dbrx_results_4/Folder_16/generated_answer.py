from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for p in permutations(s, 124):
        substring = ''.join(p)
        if len(substring) == 124 and len(set(substring)) == 124:
            result.add(substring)
    return list(result)