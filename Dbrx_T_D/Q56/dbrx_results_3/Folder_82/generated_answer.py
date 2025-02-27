from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 100 + 1):
        substring = s[i:i + 100]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return list(set(result))