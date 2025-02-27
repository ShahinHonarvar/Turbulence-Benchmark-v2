import itertools
  from collections import Counter

def palindromes_between_indices(string):
    letters = []
    for i in range(3, 6):
        if string[i].isalpha():
            letters.append(string[i].lower())
    palindromes = set()
    for i in range(4, len(letters) + 1):
        for permutation in itertools.permutations(letters, i):
            word = ''.join(permutation)
            if word == word[::-1] and len(word) >= 4:
                palindromes.add(word)
    return palindromes