from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter([char.lower() for char in string[:6] if char.isalpha()])
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for candidate in permutations(letters.elements(), length):
            word = ''.join(candidate)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes