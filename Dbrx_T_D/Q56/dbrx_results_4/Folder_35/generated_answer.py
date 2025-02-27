from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 27 + 1):
        substring = s[i:i + 27]
        if len(substring) == 27 and len(set(substring)) == 27:
            result.append(''.join(substring))
    return list(set(result))