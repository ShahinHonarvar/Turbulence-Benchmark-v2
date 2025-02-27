import re
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(sorted(re.findall('[a-zA-Z]', string[3:5])))
    palindromes = set()
    if len(letters) < 3:
        return palindromes
    for i in range(3, len(letters) + 1):
        for permutation in permutations(letters, i):
            word = ''.join(permutation)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes