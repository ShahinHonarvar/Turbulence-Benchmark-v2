import re
  from itertools import permutations

def palindromes_between_indices(string):
    s = ''.join(sorted(set(re.sub('[^a-zA-Z]+', '', string[5:9]).lower())))
    if len(s) < 3:
        return set()
    result = set()
    for i in range(3, len(s) + 1):
        for p in permutations(s, i):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result