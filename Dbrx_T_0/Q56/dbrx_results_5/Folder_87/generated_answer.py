from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 57):
        substr = ''.join((c for c in s[i:i + 58] if c not in result))
        if len(substr) == 58:
            result.append(substr)
    return list(set(result))