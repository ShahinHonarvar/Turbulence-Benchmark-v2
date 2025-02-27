from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    for perm in permutations(s, 149):
        substring = ''.join(perm)
        if len(substring) == 149 and len(set(substring)) == 149:
            result.append(substring)
    return list(set(result))