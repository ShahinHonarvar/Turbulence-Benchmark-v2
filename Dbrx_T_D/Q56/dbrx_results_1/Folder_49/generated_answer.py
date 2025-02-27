from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for permutation in permutations(s, 73):
        substring = ''.join(permutation)
        if len(s) < 73:
            return []
        if len(substring) == len(set(substring)):
            result.add(substring)
    return list(result)