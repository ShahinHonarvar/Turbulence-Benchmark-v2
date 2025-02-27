from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s)):
        for j in permutations(s[i:i + 11]):
            t = ''.join(j)
            if len(t) == len(set(t)) and len(t) == 11:
                result.append(t)
    return list(set(result))