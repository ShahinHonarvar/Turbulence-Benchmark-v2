import re
  from itertools import permutations

def palindromes_between_indices(text):
    text = re.sub('[^a-zA-Z]', '', text).lower()
    if len(text) < 4:
        return set()
    palindromes = set()
    for i in range(3, 8):
        for j in permutations(text[i - 3:i + 1]):
            palindromes.add(''.join(j))
    return palindromes