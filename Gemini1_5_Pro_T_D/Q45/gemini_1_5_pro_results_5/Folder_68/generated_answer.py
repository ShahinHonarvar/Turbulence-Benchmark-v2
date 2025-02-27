import re
  from itertools import permutations

def palindromes_between_indices(text):
    letters = ''.join(sorted(set(re.sub('[^a-zA-Z]+', '', text[1:9]).lower())))
    palindromes = set()
    for i in range(4, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes