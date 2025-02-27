from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    for perm in permutations(s, 53):
        substring = ''.join(perm)
        if len(set(substring)) == len(substring):
            result.append(substring)
    return list(set(result))