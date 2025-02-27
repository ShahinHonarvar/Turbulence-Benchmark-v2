from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 9):
        substring = s[i:i + 10]
        if len(substring) == 10 and len(set(substring)) == 10:
            result.append(substring)
    return list(set(result))