from collections import Counter
  from itertools import permutations

def palindromes_between_indices(text):
    letters = Counter([x.lower() for x in text[:8] if x.isalpha()])
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for j in permutations(letters.elements(), i):
            word = ''.join(j)
            if word == word[::-1] and len(word) >= 6:
                palindromes.add(word)
    return palindromes