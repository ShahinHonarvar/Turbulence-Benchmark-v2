import re
  from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(re.findall('[a-zA-Z]', string[3:10]))
    result = set()
    for i in range(3, len(letters) + 1):
        for candidate in permutations(letters, i):
            word = ''.join(candidate)
            if word.lower() == word[::-1].lower():
                result.add(word.lower())
    return result