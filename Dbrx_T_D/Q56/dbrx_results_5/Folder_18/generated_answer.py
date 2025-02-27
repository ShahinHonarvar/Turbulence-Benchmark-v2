from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 62):
        substring = ''.join(combinations(s[i:i + 63], 1))
        if len(substring) == 63 and all((substring.count(c) == 1 for c in substring)):
            result.append(substring)
    return list(set(result))