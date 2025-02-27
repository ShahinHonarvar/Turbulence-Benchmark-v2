from collections import Counter
  from itertools import permutations

def palindromes_between_indices(text):
    text = text.lower()
    letters = ''.join((c for c in text[3:10] if c.isalpha()))
    result = set()
    for i in range(5, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1] and word not in result:
                result.add(word)
    return result