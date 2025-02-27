import itertools
  from collections import Counter

def palindromes_between_indices(text):
    letters = ''.join((c for c in text[4:9] if c.isalpha())).lower()
    palindromes = set()
    for i in range(6, len(letters) + 1):
        for p in itertools.permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1] and Counter(word) <= Counter(letters):
                palindromes.add(word)
    return palindromes