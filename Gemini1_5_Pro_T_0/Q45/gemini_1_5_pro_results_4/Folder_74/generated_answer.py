from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter(string[1:7].lower())
    palindromes = set()
    for i in range(6, len(letters) + 1):
        for perm in permutations(letters.elements(), i):
            word = ''.join(perm)
            if word == word[::-1] and len(word) >= 6:
                palindromes.add(word)
    return palindromes