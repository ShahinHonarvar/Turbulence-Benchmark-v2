import re
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(sorted(re.sub('[^a-zA-Z]+', '', string[3:6])))
    result = set()
    if len(letters) >= 3:
        for i in range(3, len(letters) + 1):
            for p in permutations(letters, i):
                word = ''.join(p)
                if word.lower() == word[::-1].lower():
                    result.add(word.lower())
    return result