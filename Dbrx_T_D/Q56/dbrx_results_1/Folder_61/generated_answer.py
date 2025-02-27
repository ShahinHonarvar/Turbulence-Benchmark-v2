from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 38):
        substring = s[i:i + 39]
        if len(substring) == 39 and len(set(substring)) == 39:
            result.append(substring)
    return list(set(result))