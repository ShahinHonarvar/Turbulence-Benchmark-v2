from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 27 + 1):
        substr = s[i:i + 27]
        if len(substr) == 27 and len(set(substr)) == 27:
            result.add(''.join(substr))
    return list(result)