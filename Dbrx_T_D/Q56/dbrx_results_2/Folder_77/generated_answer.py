from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    if len(s) < 144:
        return result
    for i in range(len(s) - 144 + 1):
        substring = s[i:i + 144]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return list(set(result))