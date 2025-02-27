from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 142):
        substring = s[i:i + 143]
        if len(substring) == 143 and len(set(substring)) == 143:
            result.append(substring)
    return list(set(result))