from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter((string[i].lower() for i in range(7) if string[i].isalpha()))
    palindromes = set()
    for i in range(7, len(letters) + 1):
        for j in permutations(''.join((k * letters[k] for k in letters)), i):
            word = ''.join(j)
            if word == word[::-1] and word not in palindromes:
                palindromes.add(word)
    return palindromes