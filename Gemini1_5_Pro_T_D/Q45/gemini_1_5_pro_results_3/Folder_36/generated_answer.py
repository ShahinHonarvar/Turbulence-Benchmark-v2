import re
  from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(re.findall('[a-zA-Z]', text[5:9]))
    result = set()
    if len(letters) >= 3:
        for i in range(3, len(letters) + 1):
            for p in permutations(letters, i):
                word = ''.join(p)
                if word.lower() == word[::-1].lower():
                    result.add(word.lower())
    return result