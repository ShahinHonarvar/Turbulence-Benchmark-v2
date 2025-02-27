import re
  from itertools import permutations

def palindromes_between_indices(text):
    text = re.sub('[^a-zA-Z]', '', text).lower()
    if len(text) < 5 or text[3:8] == text[3:8][::-1]:
        return set()
    return {''.join(p) for p in permutations(text[3:8]) if p == p[::-1]}