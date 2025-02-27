from itertools import permutations

def palindromes_between_indices(s):
    sub = s[1:6].lower()
    alpha_sub = ''.join((c for c in sub if c.isalpha()))
    words = [''.join(p) for p in permutations(alpha_sub, len(alpha_sub))]
    palindromes = [word for word in words if word == word[::-1] and len(word) >= 5]
    return set(palindromes)