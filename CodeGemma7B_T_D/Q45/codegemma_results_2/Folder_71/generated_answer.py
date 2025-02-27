from itertools import permutations
            from string import ascii_lowercase

def palindromes_between_indices(s):
    s = s.lower()
    p = permutations(s[1:4])
    return set([''.join(i) for i in p if i == i[::-1]])