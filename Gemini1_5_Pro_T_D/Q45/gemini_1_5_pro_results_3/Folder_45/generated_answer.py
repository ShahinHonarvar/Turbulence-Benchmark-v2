from collections import Counter
  from itertools import permutations

def palindromes_between_indices(text):
    s = text[5:10]
    letters = Counter((c.lower() for c in s if c.isalpha()))
    palindromes = set()
    for i in range(4, len(s) + 1):
        for p in permutations(letters.elements(), i):
            word = ''.join(p)
            if word == word[::-1] and word.lower() not in palindromes:
                palindromes.add(word.lower())
    return palindromes