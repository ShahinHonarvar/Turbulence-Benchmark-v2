from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    if len(s) < 57:
        return result
    for i in range(len(s) - 56):
        substring = s[i:i + 57]
        if len(substring) == 57 and len(set(substring)) == 57:
            result.append(substring)
    return list(set(result))