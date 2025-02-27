import re
  from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(sorted(re.findall('[a-zA-Z]', text[3:9])))
    result = set()
    if len(letters) >= 4:
        for i in range(4, len(letters) + 1):
            for item in permutations(letters, i):
                word = ''.join(item)
                if word == word[::-1]:
                    result.add(word)
    return result