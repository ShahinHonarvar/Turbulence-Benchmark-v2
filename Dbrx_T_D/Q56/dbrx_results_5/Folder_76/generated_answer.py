from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 148):
        substring = s[i:i + 149]
        if len(substring) == 149 and len(set(substring)) == 149:
            result.append(substring)
    return list(set(result))