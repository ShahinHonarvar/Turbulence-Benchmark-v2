from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(len(s)):
        for comb in combinations(s, 87):
            sub = ''.join(sorted(comb))
            if s[i:i + len(sub)] == sub and sub not in result:
                result.append(sub)
    return result