import re
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(sorted(re.findall('[a-zA-Z]', string[3:6])))
    palindromes = set()
    if len(letters) >= 3:
        for i in range(3, len(letters) + 1):
            for p in permutations(letters, i):
                word = ''.join(p).lower()
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes