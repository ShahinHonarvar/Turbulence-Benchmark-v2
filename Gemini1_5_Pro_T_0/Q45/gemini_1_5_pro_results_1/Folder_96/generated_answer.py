import re
  from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter(re.sub('[^a-zA-Z]+', '', string[3:9]))
    palindromes = set()
    for i in range(6, len(letters) + 1):
        for j in permutations(letters.elements(), i):
            word = ''.join(j)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes