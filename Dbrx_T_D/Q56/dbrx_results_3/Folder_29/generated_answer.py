from itertools import permutations

def all_substring_of_size_n(s):
    result = []
    if len(s) < 95:
        return result
    for i in range(len(s) - 94):
        for perm in permutations(s[i:i + 95]):
            substring = ''.join(perm)
            if substring not in result and len(set(substring)) == 95:
                result.append(substring)
    return result