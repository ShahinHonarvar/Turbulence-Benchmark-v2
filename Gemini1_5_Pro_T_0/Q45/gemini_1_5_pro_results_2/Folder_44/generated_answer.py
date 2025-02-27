import re
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(sorted(re.sub('[^a-zA-Z]+', '', string[2:8]).lower()))
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes