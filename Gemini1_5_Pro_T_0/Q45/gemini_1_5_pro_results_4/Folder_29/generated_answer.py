import re
  from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter(re.sub('[^a-zA-Z]', '', string[2:10]))
    palindromes = set()
    if len(letters) >= 3:
        for i in range(3, len(letters) + 1):
            for j in permutations(letters.keys(), i):
                word = ''.join(j)
                if word == word[::-1] and len(word) >= 6:
                    palindromes.add(word.lower())
    return palindromes