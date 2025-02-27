import re
  from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(re.findall('[a-zA-Z]', text[6:10]))
    result = set()
    if len(letters) >= 4:
        for i in range(4, len(letters) + 1):
            for item in permutations(letters, i):
                word = ''.join(item)
                if word.lower() == word[::-1].lower():
                    result.add(word.lower())
    return result