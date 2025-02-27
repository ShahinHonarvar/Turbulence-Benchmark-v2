from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter((string[i].lower() for i in range(0, 7) if string[i].isalpha()))
    palindromes = set()
    for i in range(6, len(string) + 1):
        for p in permutations(letters.elements(), i):
            word = ''.join(p)
            if word == word[::-1] and len(word) >= 6:
                palindromes.add(word)
    return palindromes