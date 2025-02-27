import re
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(sorted(set(re.sub('[^a-zA-Z]', '', string[3:10]).lower())))
    palindromes = set()
    for i in range(5, len(letters) + 1):
        for permutation in permutations(letters, i):
            word = ''.join(permutation)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes