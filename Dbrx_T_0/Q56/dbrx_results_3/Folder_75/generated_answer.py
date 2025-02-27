from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 15):
        substring = s[i:i + 16]
        if len(substring) == 16 and len(set(substring)) == 16:
            result.append(substring)
    return list(set(result))