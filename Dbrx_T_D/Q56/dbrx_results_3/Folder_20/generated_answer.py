from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 50 + 1):
        substring = s[i:i + 50]
        if len(substring) == 50 and len(set(substring)) == 50:
            result.add(substring)
    return list(result)