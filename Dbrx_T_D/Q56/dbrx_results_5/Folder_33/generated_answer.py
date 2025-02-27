from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for p in permutations(s, 105):
        substring = ''.join(p)
        if len(set(substring)) == 105:
            result.add(substring)
    return list(result)