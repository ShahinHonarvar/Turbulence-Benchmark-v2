from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    for perm in permutations(s, 26):
        substring = ''.join(perm)
        if len(substring) == 26 and len(set(substring)) == 26 and (substring not in result):
            result.append(substring)
    return result