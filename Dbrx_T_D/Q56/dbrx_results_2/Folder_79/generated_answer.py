import itertools

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 60):
        substring = s[i:i + 61]
        if len(substring) == 61 and len(set(substring)) == 61:
            result.append(substring)
    return list(set(result))