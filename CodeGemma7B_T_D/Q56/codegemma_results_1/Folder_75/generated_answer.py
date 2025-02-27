from itertools import combinations

def all_substring_of_size_n(string):
    result = set()
    for substring in combinations(string, 16):
        if len(set(substring)) == 16:
            result.add(''.join(substring))
    return list(result)