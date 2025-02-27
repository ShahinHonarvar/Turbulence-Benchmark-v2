from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    for perm in permutations(s, 86):
        substring = ''.join(perm)
        if len(substring) == len(set(substring)) and substring not in result:
            result.append(substring)
    return result