from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 56):
        substring = ''.join((c for c in s[i:i + 57] if s[i:i + 57].count(c) == 1))
        if len(substring) == 57:
            result.append(substring)
    return list(set(result))