from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter((string[i].lower() for i in range(0, 9) if string[i].isalpha()))
    palindromes = set()
    for length in range(7, sum(letters.values()) + 1):
        for combination in permutations(letters.elements(), length):
            word = ''.join(combination)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes