from collections import Counter
  from itertools import permutations

def palindromes_between_indices(text):
    letters = Counter([c.lower() for c in text[:7] if c.isalpha()])
    palindromes = set()
    for perm in permutations(''.join(letters.elements())):
        word = ''.join(perm)
        if len(word) >= 7 and word == word[::-1]:
            palindromes.add(word)
    return palindromes