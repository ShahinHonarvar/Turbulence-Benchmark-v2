from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 32 + 1):
        substring = s[i:i + 32]
        if len(substring) == 32 and len(set(substring)) == 32:
            result.append(substring)
    return list(set(result))