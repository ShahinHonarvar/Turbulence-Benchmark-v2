from itertools import permutations

def palindromes_between_indices(s):
    sub_str = ''.join(filter(str.isalpha, s[1:6])).lower()
    all_permutations = set((''.join(p) for p in permutations(sub_str)))
    palindromes = set()
    for perm in all_permutations:
        for i in range(len(perm) - 4):
            sub_perm = perm[i:i + 5]
            if sub_perm == sub_perm[::-1]:
                palindromes.add(sub_perm)
    return palindromes