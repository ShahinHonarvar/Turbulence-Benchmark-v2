from itertools import permutations

def all_substring_of_size_n(s):
    result = set()
    for i in range(142, len(s)):
        for j in permutations(s[i - 142:i]):
            substring = ''.join(j)
            if len(substring) == 142 and len(set(substring)) == 142:
                result.add(substring)
    return list(result)