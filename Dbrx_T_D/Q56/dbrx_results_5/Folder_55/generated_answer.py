from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 40 + 1):
        substr = s[i:i + 40]
        if len(substr) == 40 and len(set(substr)) == 40:
            result.append(''.join(substr))
    return list(set(result))