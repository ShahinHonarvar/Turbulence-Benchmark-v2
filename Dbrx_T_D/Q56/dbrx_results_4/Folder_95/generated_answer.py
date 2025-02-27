from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 89 + 1):
        substring = s[i:i + 89]
        if len(substring) == 89 and len(set(substring)) == 89:
            result.append(substring)
    return list(set(result))