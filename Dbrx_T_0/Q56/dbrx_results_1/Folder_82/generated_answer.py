from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 100):
        substring = s[i:i + 100]
        if len(substring) == 100 and len(set(substring)) == 100:
            result.append(substring)
    return list(set(result))