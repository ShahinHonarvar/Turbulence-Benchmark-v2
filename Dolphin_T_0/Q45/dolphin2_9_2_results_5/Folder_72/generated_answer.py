import itertools

def palindromes_between_indices(s):
    indices = list(range(1, 8))
    substrings = [''.join((s[i] for i in indices)) for indices in itertools.permutations(indices)]
    palindromes = {s.lower(): s for s in substrings if len(set(s)) >= 6 and s == s[::-1]}
    return palindromes