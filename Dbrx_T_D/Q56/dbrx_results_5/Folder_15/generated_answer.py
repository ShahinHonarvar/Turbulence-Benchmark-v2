from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s) - 2):
        for j in combinations(s[i + 1:], 2):
            substring = s[i] + ''.join(sorted(j))
            if substring not in result:
                result.append(substring)
    return result