import re
from functools import reduce

def palindromes_between_indices(s):
    alpha = re.sub('[^a-zA-Z]', '', s[5:10])
    if len(alpha) < 4:
        return set()
    chars = list(set(alpha.lower()))
    palindromes = [reduce(lambda x, y: x + y, p) for n in range(4, len(chars) + 1) for p in itertools.permutations(chars, n) if reduce(lambda x, y: x + y, p) == reduce(lambda x, y: x + y, p[::-1])]
    return set(palindromes)