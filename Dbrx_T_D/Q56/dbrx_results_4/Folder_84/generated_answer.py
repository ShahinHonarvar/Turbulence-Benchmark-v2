from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 113):
        substr = s[i:i + 114]
        if len(substr) == 114 and len(set(substr)) == 114:
            result.append(''.join(substr))
    return list(set(result))