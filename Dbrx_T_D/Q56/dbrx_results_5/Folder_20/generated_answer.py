from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 49):
        substring = s[i:i + 50]
        if len(substring) == 50 and len(set(substring)) == 50:
            result.append(substring)
    return list(set(result))