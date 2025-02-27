from itertools import permutations

def palindromes_between_indices(s):
    sub_s = ''.join(list(filter(str.isalpha, s[2:10])))
    sub_s_permutations = [''.join(p) for p in permutations(sub_s)]
    palindromes = [p for p in sub_s_permutations if len(p) >= 5 and p.lower() == p[::-1].lower()]
    return set(palindromes)