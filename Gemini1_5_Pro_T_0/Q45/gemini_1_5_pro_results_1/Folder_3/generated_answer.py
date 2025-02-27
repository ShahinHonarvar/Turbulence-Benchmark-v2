import re
  from itertools import permutations

def palindromes_between_indices(string):
    result = set()
    for item in permutations(re.findall('[a-zA-Z]', string[7:10])):
        word = ''.join(item)
        if len(word) >= 3 and word.lower() == word[::-1].lower():
            result.add(word.lower())
    return result