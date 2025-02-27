import re
  from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(sorted(re.findall('[a-zA-Z]', text[2:6])))
    result = set()
    if len(letters) < 3:
        return result
    for i in range(3, len(letters) + 1):
        for j in permutations(letters, i):
            word = ''.join(j)
            if word == word[::-1]:
                result.add(word)
    return result