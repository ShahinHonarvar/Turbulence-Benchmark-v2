from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 11):
        substr = ''.join(combinations(s[i:i + 12], 12))
        if len(substr) == 12:
            if substr not in result:
                result.append(substr)
    return result