from itertools import combinations_with_replacement

def all_substring_of_size_n(str1):
    result = []
    for x in combinations_with_replacement(str1, 58):
        result.append(''.join(map(str, x)))
    return result