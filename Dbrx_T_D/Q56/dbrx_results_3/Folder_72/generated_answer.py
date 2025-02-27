from itertools import combinations

def all_substring_of_size_n(s):
    result = []
    for i in range(1, len(s) - 87):
        for comb in combinations(s[i:i + 88], 88):
            if len(set(comb)) == 88:
                result.append(''.join(comb))
    return list(set(result))