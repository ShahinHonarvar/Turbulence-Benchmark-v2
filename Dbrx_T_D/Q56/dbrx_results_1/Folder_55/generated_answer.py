from itertools import combinations

def all_substrings_of_size_n(s):
    result = []
    for i in range(len(s) - 39):
        substring = s[i:i + 40]
        if len(set(substring)) == 40:
            result.append(substring)
    return list(set(result))