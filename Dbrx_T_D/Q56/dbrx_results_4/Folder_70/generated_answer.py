from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 11):
        for perm in permutations(s[i:i + 12]):
            substring = ''.join(perm)
            if len(substring) == 12 and len(set(substring)) == 12 and (substring not in result):
                result.append(substring)
    return result