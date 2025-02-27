from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 40):
        substring = ''.join((c for c in s[i:i + 41] if s[i:i + 41].count(c) == 1))
        if len(substring) == 41:
            result.append(substring)
    return list(set(result))