from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    for permutation in permutations(s, 26):
        substring = ''.join(permutation)
        if len(set(substring)) == 26 and substring not in result:
            result.append(substring)
    return result