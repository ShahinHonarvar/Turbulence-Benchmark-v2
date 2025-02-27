import re
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(sorted(re.findall('[a-zA-Z]', string[5:10])))
    if len(letters) < 5:
        return set()
    result = set()
    for i in range(5, len(letters) + 1):
        for item in permutations(letters, i):
            word = ''.join(item)
            if word.lower() == word[::-1].lower():
                result.add(word)
    return result