from itertools import permutations

def palindromes_between_indices(s):
    substr = s[1:7].lower()
    substr = ''.join(filter(str.isalpha, substr))
    palindromes = set()
    for p in permutations(substr):
        p_str = ''.join(p)
        if len(p_str) >= 6 and p_str == p_str[::-1]:
            palindromes.add(p_str)
    return palindromes