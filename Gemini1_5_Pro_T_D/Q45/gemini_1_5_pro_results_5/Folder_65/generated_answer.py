from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter((string[i].lower() for i in range(7) if string[i].isalpha()))
    palindromes = set()
    for length in range(5, len(letters) + 1):
        for candidate in permutations(letters.elements(), length):
            word = ''.join(candidate)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes