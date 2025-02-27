from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 91):
        for perm in permutations(s[i:i + 92]):
            substr = ''.join(perm)
            if len(substr) == len(set(substr)):
                result.add(substr)
    return list(result)