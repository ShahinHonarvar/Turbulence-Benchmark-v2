from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = ''.join((c for c in string[2:9] if c.isalpha())).lower()
    possible_palindromes = set()
    for i in range(7, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                possible_palindromes.add(word)
    return possible_palindromes