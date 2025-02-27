from itertools import permutations

def palindromes_between_indices(s):
    palindromes = set()
    distinct_letters = set(s[4:10].lower())
    for p in permutations(distinct_letters, length):
        permutation_str = ''.join(p)
        if permutation_str == permutation_str[::-1] and len(permutation_str) >= 5:
            palindromes.add(permutation_str)
    return palindromes