from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 8):
        for perm in permutations(s[i:i + 9]):
            substring = ''.join(perm)
            if len(substring) == len(set(substring)):
                result.append(substring)
    return list(set(result))