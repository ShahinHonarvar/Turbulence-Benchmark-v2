from itertools import combinations

def all_substrings_of_size_n(s):
    result = []
    for chars in combinations(s, 33):
        substring = ''.join(chars)
        if len(substring) == len(set(substring)):
            result.append(substring)
    return result