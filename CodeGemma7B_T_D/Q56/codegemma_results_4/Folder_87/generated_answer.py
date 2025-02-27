from itertools import combinations

def all_substring_of_size_n(string):
    result = set()
    for combination in combinations(range(len(string)), 58):
        result.add(''.join((string[i] for i in combination)))
    return list(result)