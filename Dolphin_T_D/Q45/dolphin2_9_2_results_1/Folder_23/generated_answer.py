from itertools import permutations

def palindromes_between_indices(s):
    letters = [c.lower() for c in s[0:7]]
    arrangements = [''.join(p) for p in permutations(letters)]
    palindromes = [a for a in arrangements if a == a[::-1] and len(a) >= 4]
    return set(palindromes)