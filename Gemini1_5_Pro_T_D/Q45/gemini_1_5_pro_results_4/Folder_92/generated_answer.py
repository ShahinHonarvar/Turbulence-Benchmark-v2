import re
  from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(sorted(set(re.sub('[^a-zA-Z]+', '', text[4:8]).lower())))
    result = set()
    if len(letters) >= 4:
        for i in range(4, len(letters) + 1):
            for p in permutations(letters, i):
                word = ''.join(p)
                if word == word[::-1]:
                    result.add(word)
    return result