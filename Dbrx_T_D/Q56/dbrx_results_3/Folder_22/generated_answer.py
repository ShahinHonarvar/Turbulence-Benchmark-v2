from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 21):
        substr = s[i:i + 22]
        if len(substr) == 22 and len(set(substr)) == 22:
            result.append(''.join(substr))
    return list(set(result))