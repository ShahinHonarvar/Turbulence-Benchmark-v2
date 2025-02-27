from itertools import combinations

def palindromes_between_indices(s):
    palindromes = set()
    for i in range(4, len(s) + 1):
        for comb in combinations(s[3:9], i):
            if ''.join(comb).lower() == ''.join(comb[::-1]).lower():
                palindromes.add(''.join(comb))
    return palindromes