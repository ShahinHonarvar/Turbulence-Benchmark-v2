from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter((c for c in string[:9] if c.isalpha()))
    palindromes = set()
    for length in range(7, sum(letters.values()) + 1):
        for combination in permutations(letters.elements(), length):
            word = ''.join(combination)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes