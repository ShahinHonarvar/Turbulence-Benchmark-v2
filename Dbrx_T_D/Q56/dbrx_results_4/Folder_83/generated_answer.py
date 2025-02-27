from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 47):
        for perm in permutations(s[i:i + 48]):
            substring = ''.join(perm)
            if len(substring) == 48 and len(set(substring)) == 48:
                result.add(substring)
    return list(result)