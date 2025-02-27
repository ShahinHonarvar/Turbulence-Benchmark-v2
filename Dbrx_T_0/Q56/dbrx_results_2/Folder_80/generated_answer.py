from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 30 + 1):
        substring = s[i:i + 31]
        if len(substring) == 31 and len(set(substring)) == 31:
            result.append(substring)
    return list(set(result))