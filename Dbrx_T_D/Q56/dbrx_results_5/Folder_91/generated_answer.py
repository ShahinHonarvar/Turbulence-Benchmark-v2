from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 5):
        for perm in permutations(s[i:i + 6]):
            substring = ''.join(perm)
            if len(substring) == 6 and len(set(substring)) == 6 and (substring not in result):
                result.append(substring)
    return result