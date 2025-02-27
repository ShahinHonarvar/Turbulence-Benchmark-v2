import itertools
  from collections import Counter

def palindromes_between_indices(string):
    letters = []
    for i in range(3, 9):
        if string[i].isalpha():
            letters.append(string[i].lower())
    result = set()
    for i in range(6, len(letters) + 1):
        for item in itertools.permutations(letters, i):
            word = ''.join(item)
            if word == word[::-1] and word not in result:
                result.add(word)
    return result