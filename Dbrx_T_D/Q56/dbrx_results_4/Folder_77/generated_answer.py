from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for perm in permutations(s, 144):
        substring = ''.join(perm)
        if len(substring) == 144 and len(set(substring)) == 144:
            result.add(substring)
    return list(result)