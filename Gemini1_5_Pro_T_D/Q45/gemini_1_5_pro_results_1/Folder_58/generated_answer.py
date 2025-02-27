from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter([x.lower() for x in string[:7] if x.isalpha()])
    palindromes = set()
    for length in range(6, len(string) + 1):
        for candidate in permutations(letters.elements(), length):
            word = ''.join(candidate)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes