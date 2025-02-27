from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 35):
        substring = s[i:i + 36]
        if len(substring) == 36 and len(set(substring)) == 36:
            result.append(substring)
    return list(set(result))