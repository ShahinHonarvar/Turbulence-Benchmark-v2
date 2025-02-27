from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter(string[2:9].lower())
    palindromes = set()
    for length in range(4, len(string) + 1):
        for candidate in permutations(letters.elements(), length):
            word = ''.join(candidate)
            if word == word[::-1] and word not in palindromes:
                palindromes.add(word)
    return palindromes