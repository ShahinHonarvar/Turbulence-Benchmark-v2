from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 33):
        substr = s[i:i + 34]
        if len(substr) == 34 and len(set(substr)) == 34:
            result.add(substr)
    return list(result)