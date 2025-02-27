import itertools
	from string import ascii_lowercase

def palindromes_between_indices(s):
    s = ''.join([c for c in s if c in ascii_lowercase])
    s = s[2:6]
    combinations = [''.join(p) for i in range(len(s)) for p in itertools.permutations(s, i + 1)]
    permutations = [''.join(p) for i in range(len(combinations)) for p in itertools.permutations(combinations[i], len(combinations[i]))]
    palindromes = [p for p in permutations if p.lower() == p.lower()[::-1] and len(p) >= 5]
    return set(palindromes)