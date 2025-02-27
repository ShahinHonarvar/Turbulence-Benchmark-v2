import re
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(sorted(set(re.sub('[^a-zA-Z]', '', string[5:10]).lower())))
    if len(letters) < 5:
        return set()
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for permutation in permutations(letters, i):
            word = ''.join(permutation)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes