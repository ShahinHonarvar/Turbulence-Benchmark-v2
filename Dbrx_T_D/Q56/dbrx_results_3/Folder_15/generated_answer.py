from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 2):
        substr = ''.join(sorted(s[i:i + 3]))
        if substr not in result:
            result.append(substr)
    return result