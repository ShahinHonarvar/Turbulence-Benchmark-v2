import re
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(sorted(set(re.sub('[^a-zA-Z]+', '', string[2:10]).lower())))
    if len(letters) < 7:
        return set()
    result = set()
    for i in range(7, len(letters) + 1):
        for j in permutations(letters, i):
            word = ''.join(j)
            if word == word[::-1]:
                result.add(word)
    return result