import re

def palindromes_between_indices(s):
    letters = re.findall('[a-zA-Z]', s[2:7])
    palindromes = {x for l in letters for x in [w for w in {x.lower() for x in [''.join(p) for i in range(4, len(s[2:7]) + 1) for p in itertools.permutations(l, i)] if x == x[::-1]} if len(x) >= 4]}
    return palindromes