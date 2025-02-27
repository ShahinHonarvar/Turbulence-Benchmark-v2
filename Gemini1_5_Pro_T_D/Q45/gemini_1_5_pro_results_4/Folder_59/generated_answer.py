import re
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join(sorted(set(re.sub('[^a-zA-Z]', '', string[8:10]).lower())))
    palindromes = set()
    if len(letters) >= 3:
        for i in range(3, len(letters) + 1):
            for permutation in permutations(letters, i):
                word = ''.join(permutation)
                if word == word[::-1]:
                    palindromes.add(word)
    return palindromes