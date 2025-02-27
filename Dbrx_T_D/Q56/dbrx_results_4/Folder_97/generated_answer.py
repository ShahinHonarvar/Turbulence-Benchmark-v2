from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 141):
        substring = s[i:i + 142]
        if len(substring) == 142 and len(set(substring)) == 142:
            result.append(''.join(substring))
    return list(set(result))