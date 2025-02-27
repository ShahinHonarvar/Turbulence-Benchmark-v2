import re
  from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(sorted(re.findall('[a-zA-Z]', text[6:10])))
    if len(letters) < 5:
        return set()
    result = set()
    for i in range(5, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                result.add(word)
    return result