import itertools
  from collections import Counter

def palindromes_between_indices(string):
    letters = ''
    for i in range(6):
        if string[i].isalpha():
            letters += string[i]
    letters = letters.lower()
    results = set()
    for i in range(6, len(letters) + 1):
        for j in itertools.permutations(letters, i):
            word = ''.join(j)
            if word == word[::-1] and len(word) >= 6:
                results.add(word)
    return results