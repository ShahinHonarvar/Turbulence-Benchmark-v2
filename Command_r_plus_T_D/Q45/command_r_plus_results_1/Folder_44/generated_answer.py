import itertools

def palindromes_between_indices(s):
    letters = [c for c in s[2:8] if c.isalpha()]
    arrangements = [''.join(p) for p in itertools.permutations(letters)]
    palindromes = set((arr for arr in arrangements if len(arr) >= 3 and arr == arr[::-1]))
    return palindromes