import re
  from collections import Counter
  from itertools import permutations

def palindromes_between_indices(text):
    letters = Counter(re.sub('[^a-zA-Z]', '', text[4:10]))
    palindromes = set()
    for i in range(7, len(letters) + 1):
        for j in permutations(letters.elements(), i):
            word = ''.join(j)
            if word == word[::-1] and len(word) >= 7:
                palindromes.add(word.lower())
    return palindromes