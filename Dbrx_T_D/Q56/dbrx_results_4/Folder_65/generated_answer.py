import itertools

def all_substring_of_size_n(s):
    result = []
    n = 81
    for i in range(len(s) - n + 1):
        substring = s[i:i + n]
        if len(substring) == len(set(substring)):
            result.append(substring)
    return list(set(result))