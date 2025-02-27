import re
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(sorted(set(re.sub('[^a-zA-Z]+', '', string[6:9]).lower())))
    return {''.join(p) for i in range(4, len(letters) + 1) for p in permutations(letters, i) if ''.join(p) == ''.join(p)[::-1]}