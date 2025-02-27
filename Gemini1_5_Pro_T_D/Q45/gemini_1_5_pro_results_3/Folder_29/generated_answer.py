import re
  from collections import Counter
from itertools import permutations

def palindromes_between_indices(string):
    letters = re.findall('[a-zA-Z]', string[2:10])
    counts = Counter(letters)
    middle = ''.join([char for char in counts if counts[char] % 2 == 1])
    half = ''.join([char * (counts[char] // 2) for char in counts])
    perms = set([''.join(perm) for perm in permutations(half)])
    if len(middle) > 1:
        return set()
    elif len(perms) > 0 and len(middle) == 1:
        return {''.join([perm + middle + perm[::-1] for perm in perms]).lower()}
    elif len(perms) > 0 and len(middle) == 0:
        return {''.join([perm + perm[::-1] for perm in perms]).lower()}
    else:
        return set()