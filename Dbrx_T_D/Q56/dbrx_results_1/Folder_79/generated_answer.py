from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    if len(s) < 61:
        return result
    for i in range(len(s) - 60):
        substring = s[i:i + 61]
        if len(substring) == 61 and len(set(substring)) == 61:
            result.append(substring)
    return list(set(result))