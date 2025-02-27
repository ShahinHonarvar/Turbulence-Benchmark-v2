from collections import Counter
  from itertools import permutations

def palindromes_between_indices(text):
    letters = Counter((c.lower() for c in text[:8] if c.isalpha()))
    palindromes = set()
    for length in range(7, len(letters) + 1):
        for candidate in permutations(letters.keys(), length):
            word = ''.join(candidate)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes