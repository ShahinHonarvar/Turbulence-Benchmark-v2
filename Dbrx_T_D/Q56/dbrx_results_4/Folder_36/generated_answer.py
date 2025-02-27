from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 146 + 1):
        substring = s[i:i + 146]
        if len(substring) == 146 and len(set(substring)) == 146:
            result.append(substring)
    return list(set(result))