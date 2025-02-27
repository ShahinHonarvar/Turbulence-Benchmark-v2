from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter([string[i].lower() for i in range(1, 4) if string[i].isalpha()])
    palindromes = set()
    for n in range(4, sum(letters.values()) + 1):
        for p in permutations(letters.elements(), n):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes