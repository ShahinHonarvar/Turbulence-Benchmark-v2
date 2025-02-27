from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 74 + 1):
        substring = s[i:i + 74]
        if len(substring) == 74 and len(set(substring)) == 74:
            result.append(''.join(substring))
    return list(set(result))