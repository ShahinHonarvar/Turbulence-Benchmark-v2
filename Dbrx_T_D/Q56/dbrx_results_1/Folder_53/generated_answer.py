from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    if len(s) < 25:
        return result
    for i in range(len(s) - 24):
        substring = s[i:i + 25]
        if len(substring) == 25 and len(set(substring)) == 25:
            result.append(substring)
    return list(set(result))