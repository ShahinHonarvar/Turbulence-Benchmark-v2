from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter((string[i].lower() for i in range(0, 7) if string[i].isalpha()))
    palindromes = set()
    if len(letters) < 7:
        return palindromes
    for i in range(7, len(letters) + 1):
        for j in permutations(letters.elements(), i):
            word = ''.join(j)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes