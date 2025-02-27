import re
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(sorted(re.sub('[^a-zA-Z]+', '', string[4:6])))
    if len(letters) < 3:
        return set()
    result = set()
    for i in range(3, len(letters) + 1):
        for j in permutations(letters, i):
            word = ''.join(j)
            if word == word[::-1]:
                result.add(word)
    return result