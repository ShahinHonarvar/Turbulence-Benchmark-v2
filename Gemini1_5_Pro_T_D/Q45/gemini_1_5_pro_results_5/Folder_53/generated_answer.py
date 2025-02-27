import re
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(sorted(set(re.sub('[^a-zA-Z]+', '', string[4:9]).lower())))
    palindromes = set()
    for i in range(len(letters) + 1):
        for j in permutations(letters, i):
            word = ''.join(j)
            if len(word) >= 6 and word == word[::-1]:
                palindromes.add(word)
    return palindromes