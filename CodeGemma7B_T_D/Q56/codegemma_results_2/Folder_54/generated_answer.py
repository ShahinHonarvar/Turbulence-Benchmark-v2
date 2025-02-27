from itertools import combinations

def all_substring_of_size_n(str):
    ans = set()
    for comb in combinations(str, 28):
        if len(set(comb)) == 28:
            ans.add(''.join(comb))
    return list(ans)