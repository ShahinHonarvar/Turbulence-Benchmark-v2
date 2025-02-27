from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 34):
        substring = s[i:i + 35]
        if len(substring) == 35 and len(set(substring)) == 35:
            result.append(substring)
    return list(set(result))