import itertools

def palindromes_between_indices(s):
    s = s[2:10].lower()
    result = {''.join(x) for i in range(6, len(s) + 1) for x in itertools.permutations(s, i) if ''.join(x) == ''.join(reversed(x))}
    return result