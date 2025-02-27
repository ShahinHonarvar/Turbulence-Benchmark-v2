from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 20 + 1):
        substring = s[i:i + 20]
        if len(substring) == 20 and len(set(substring)) == 20:
            result.append(substring)
    return list(set(result))