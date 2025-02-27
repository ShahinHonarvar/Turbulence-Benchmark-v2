from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 70 + 1):
        substring = s[i:i + 70]
        if len(substring) == len(set(substring)):
            result.add(substring)
    return list(result)