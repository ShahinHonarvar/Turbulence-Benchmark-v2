from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for permutation in permutations(s, 127):
        substring = ''.join(permutation)
        if len(set(substring)) == len(substring):
            result.add(substring)
    return list(result)