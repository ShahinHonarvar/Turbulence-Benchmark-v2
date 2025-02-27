from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter((string[i].lower() for i in range(7) if string[i].isalpha()))
    palindromes = set()
    for p in permutations(''.join((letter * count for letter, count in letters.items()))):
        word = ''.join(p)
        if len(word) >= 7 and word == word[::-1]:
            palindromes.add(word)
    return palindromes