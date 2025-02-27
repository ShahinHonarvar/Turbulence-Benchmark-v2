from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 37 + 1):
        substring = s[i:i + 37]
        if len(substring) == 37 and len(set(substring)) == 37:
            result.append(substring)
    return list(set(result))