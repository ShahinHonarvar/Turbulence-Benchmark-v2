from itertools import combinations

def palindromes_between_indices(s):
    substring = s[0:8].lower()
    palindromes = set()
    for r in range(6, len(substring) + 1):
        combinations_list = combinations(substring, r)
        for combination in combinations_list:
            if combination == combination[::-1]:
                palindromes.add(''.join(combination))
    return palindromes