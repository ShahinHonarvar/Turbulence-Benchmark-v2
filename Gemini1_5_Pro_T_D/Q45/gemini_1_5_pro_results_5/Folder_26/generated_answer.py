import re
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(sorted(set(re.findall('[a-zA-Z]', string[4:7]))))
    if len(letters) < 3:
        return set()
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes