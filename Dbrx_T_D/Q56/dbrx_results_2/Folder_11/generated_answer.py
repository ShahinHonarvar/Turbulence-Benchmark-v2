import itertools

def all_substring_of_size_n(s):
    result = []
    if len(s) < 78 or len(set(s)) < 78:
        return result
    for i in range(len(s) - 78 + 1):
        substring = s[i:i + 78]
        if len(set(substring)) == 78:
            result.append(substring)
    return list(set(result))