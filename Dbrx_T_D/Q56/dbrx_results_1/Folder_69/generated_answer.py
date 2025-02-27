from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 98):
        substring = s[i:i + 99]
        if len(substring) == 99 and len(set(substring)) == 99:
            result.append(''.join(substring))
    return list(set(result))