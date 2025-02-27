from itertools import permutations
    import re

def palindromes_between_indices(string):
    string = re.sub('[^a-zA-Z]', '', string)
    indices = range(1, 9)
    sub = [string[i] for i in indices]
    sub_permutations = set((''.join(p) for p in permutations(sub)))
    palindromes = set((s for s in sub_permutations if re.match('^(.)(.)?(.)\\2\\1$', s, re.IGNORECASE)))
    return palindromes