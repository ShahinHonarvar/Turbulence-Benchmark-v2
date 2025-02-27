from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter((string[i].lower() for i in range(0, 7) if string[i].isalpha()))
    palindromes = set()
    if len(letters) < 3:
        return palindromes
    for i in range(3, len(letters) + 1):
        for j in permutations(letters.keys(), i):
            word = ''.join(j)
            if word[::-1] == word and word not in palindromes:
                palindromes.add(word)
    return palindromes