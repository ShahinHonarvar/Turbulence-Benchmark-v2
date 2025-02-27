import re
  from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = re.findall('[a-zA-Z]', string[5:9])
    palindromes = set()
    for n in range(3, len(letters) + 1):
        for p in permutations(letters, n):
            word = ''.join(p)
            if word.lower() == word[::-1].lower():
                palindromes.add(word.lower())
    return palindromes