from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter([string[i].lower() for i in range(6) if string[i].isalpha()])
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for j in permutations(letters.elements(), i):
            word = ''.join(j)
            if word == word[::-1] and len(word) >= 6:
                palindromes.add(word)
    return palindromes