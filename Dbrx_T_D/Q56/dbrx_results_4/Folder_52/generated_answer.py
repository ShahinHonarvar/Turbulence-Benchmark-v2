from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 14):
        substr = s[i:i + 15]
        if len(substr) == 15 and len(set(substr)) == 15:
            result.append(''.join(substr))
    return list(set(result))