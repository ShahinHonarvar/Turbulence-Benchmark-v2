import re
  from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(sorted(set(re.sub('[^a-zA-Z]+', '', text[0:8]).lower())))
    result = set()
    for i in range(4, len(letters) + 1):
        for p in permutations(letters, i):
            candidate = ''.join(p)
            if candidate == candidate[::-1]:
                result.add(candidate)
    return result