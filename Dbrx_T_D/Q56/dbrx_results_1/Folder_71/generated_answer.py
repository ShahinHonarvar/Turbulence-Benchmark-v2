from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 16):
        substring = s[i:i + 17]
        if len(substring) == 17 and len(set(substring)) == 17:
            result.append(substring)
    return list(set(result))