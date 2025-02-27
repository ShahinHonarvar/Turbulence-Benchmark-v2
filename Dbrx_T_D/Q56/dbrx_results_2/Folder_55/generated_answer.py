from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 40 + 1):
        substring = s[i:i + 40]
        if len(substring) == 40 and len(set(substring)) == 40:
            result.append(substring)
    return list(set(result))