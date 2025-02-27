from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for perm in permutations(s, 91):
        substring = ''.join(perm)
        if len(set(substring)) == 91:
            result.add(substring)
    return list(result)