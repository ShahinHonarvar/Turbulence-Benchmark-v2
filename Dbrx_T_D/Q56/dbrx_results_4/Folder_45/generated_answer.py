from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 29 + 1):
        substring = s[i:i + 29]
        if len(substring) == 29 and len(set(substring)) == 29:
            result.append(''.join(substring))
    return list(set(result))