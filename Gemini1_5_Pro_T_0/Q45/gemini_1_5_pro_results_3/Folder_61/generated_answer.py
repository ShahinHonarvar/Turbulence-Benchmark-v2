from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter((string[i].lower() for i in range(0, 8) if string[i].isalpha()))
    palindromes = set()
    for i in range(7, len(string) + 1, 2):
        for candidate in permutations(letters.elements(), i):
            word = ''.join(candidate)
            if word == word[::-1] and len(word) >= 7:
                palindromes.add(word)
    return palindromes