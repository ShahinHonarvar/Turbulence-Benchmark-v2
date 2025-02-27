import itertools
  from collections import Counter

def palindromes_between_indices(string):
    letters = []
    for i in range(3, 8):
        if string[i].isalpha() and string[i].lower() in 'abcdefghijklmnopqrstuvwxyz':
            letters.append(string[i].lower())
    result = set()
    for i in range(5, len(letters) + 1):
        for permutation in itertools.permutations(letters, i):
            word = ''.join(permutation)
            if word == word[::-1] and len(word) >= 5:
                result.add(word)
    return result