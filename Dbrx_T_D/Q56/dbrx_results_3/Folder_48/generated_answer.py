from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s) - 119):
        for perm in permutations(s[i:i + 120]):
            substring = ''.join(perm)
            if len(substring) == 120 and len(set(substring)) == 120:
                result.add(substring)
    return list(result)