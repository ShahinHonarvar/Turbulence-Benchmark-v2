import re
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(sorted(set(re.findall('[a-zA-Z]', string[6:10])), key=str.casefold))
    return {''.join(p) for i in range(5, len(letters) + 1) for p in permutations(letters, i) if ''.join(p) == ''.join(reversed(''.join(p)))}