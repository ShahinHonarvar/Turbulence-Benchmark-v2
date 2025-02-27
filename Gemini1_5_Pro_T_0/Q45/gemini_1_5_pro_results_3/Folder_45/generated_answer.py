import re
  from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(re.findall('[a-zA-Z]', string[5:10]))
    palindromes = set()
    for i in range(4, len(letters) + 1):
        for p in permutations(letters.lower(), i):
            word = ''.join(p)
            if word == word[::-1] and word not in palindromes:
                palindromes.add(word)
    return palindromes