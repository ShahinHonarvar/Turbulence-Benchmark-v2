from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 55):
        substring = ''.join((c for c in s[i:i + 56] if c not in result))
        if len(substring) == 56 and all((substring.count(c) == 1 for c in substring)):
            result.append(substring)
    return list(set(result))