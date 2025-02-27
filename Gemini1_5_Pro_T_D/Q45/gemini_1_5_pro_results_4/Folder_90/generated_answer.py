from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = set([char.lower() for char in string[:6] if char.isalpha()])
    result = set()
    for length in range(4, len(letters) + 1):
        for candidate in permutations(letters, length):
            word = ''.join(candidate)
            if word == word[::-1]:
                result.add(word)
    return result