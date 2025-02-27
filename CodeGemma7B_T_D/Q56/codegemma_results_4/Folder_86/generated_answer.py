from itertools import combinations_with_replacement

def all_substring_of_size_n(string):
    if len(string) < 143:
        return []
    result = []
    for i in range(len(string) - 142):
        substring = string[i:i + 143]
        if len(set(substring)) == 143:
            result.append(substring)
    return result