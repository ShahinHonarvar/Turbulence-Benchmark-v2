from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 18):
        substr = s[i:i + 19]
        if len(substr) == 19 and len(set(substr)) == 19:
            result.append(''.join(substr))
    return list(set(result))