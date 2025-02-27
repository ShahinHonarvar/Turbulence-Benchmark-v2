from itertools import permutations
  from collections import Counter

def palindromes_between_indices(string):
    letters = [string[i].lower() for i in range(1, 8) if string[i].isalpha()]
    palindromes = set()
    for i in range(6, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes