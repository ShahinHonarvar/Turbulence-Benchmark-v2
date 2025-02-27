import itertools

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 43):
        substring = s[i:i + 44]
        if len(set(substring)) == 44:
            result.append(substring)
    return list(set(result))