from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 26):
        substr = ''.join((c for c in s[i:i + 27] if c not in result))
        if len(substr) == 27 and all((substr.count(c) == 1 for c in substr)):
            result.append(substr)
    return list(set(result))