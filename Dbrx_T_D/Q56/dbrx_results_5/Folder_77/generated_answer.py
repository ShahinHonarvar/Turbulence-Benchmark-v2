from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 144 + 1):
        substring = s[i:i + 144]
        if len(set(substring)) == 144:
            result.add(substring)
    return list(result)