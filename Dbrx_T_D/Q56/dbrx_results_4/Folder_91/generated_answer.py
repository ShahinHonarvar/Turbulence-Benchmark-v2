from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 5):
        for perm in permutations(s[i:i + 6]):
            substring = ''.join(perm)
            if len(substring) == 6 and len(set(substring)) == 6:
                result.add(substring)
    return list(result)