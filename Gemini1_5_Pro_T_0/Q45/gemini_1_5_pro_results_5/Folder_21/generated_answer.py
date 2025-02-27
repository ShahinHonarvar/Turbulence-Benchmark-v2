import re
  from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(sorted(re.findall('[a-zA-Z]', text[1:9])))
    return {''.join(p) for i in range(7, len(letters) + 1) for p in permutations(letters, i) if ''.join(p) == ''.join(reversed(''.join(p)))}