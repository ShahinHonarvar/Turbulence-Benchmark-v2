import itertools

def palindromes_between_indices(s):
    chars = [c.lower() for c in s if c.isalpha()]
    subchars = chars[2:9]
    arrangements = itertools.permutations(subchars, len(subchars))
    palindromes = [x for x in [''.join(arr) for arr in arrangements] if len(x) >= 6 and x == x[::-1]]
    return set(palindromes)