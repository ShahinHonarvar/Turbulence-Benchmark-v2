import itertools

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 68):
        substring = s[i:i + 69]
        if len(substring) == 69 and len(set(substring)) == 69:
            result.append(substring)
    return list(set(result))