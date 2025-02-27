from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(len(s)):
        for perm in permutations(s[i:i + 105]):
            substring = ''.join(perm)
            if len(substring) == 105 and len(set(substring)) == 105:
                result.add(substring)
    return list(result)