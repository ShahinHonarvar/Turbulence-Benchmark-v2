from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 90):
        substr = ''.join(combinations(s[i:i + 91], 1))
        if len(substr) == 91 and substr not in result:
            result.append(substr)
    return result