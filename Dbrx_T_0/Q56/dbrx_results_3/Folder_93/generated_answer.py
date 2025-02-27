from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 54 + 1):
        substring = s[i:i + 54]
        if len(substring) == 54 and len(set(substring)) == 54:
            result.append(substring)
    return list(set(result))