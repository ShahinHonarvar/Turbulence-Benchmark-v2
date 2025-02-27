from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 23):
        for perm in permutations(s[i:i + 24]):
            substring = ''.join(perm)
            if len(substring) == 24 and len(set(substring)) == 24:
                result.add(substring)
    return list(result)