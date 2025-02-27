import re
  from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(sorted(set(re.sub('[^a-zA-Z]+', '', text[2:10]).lower())))
    return {''.join(p) for i in range(6, len(letters) + 1) for p in permutations(letters, i) if ''.join(p) == ''.join(p)[::-1]}