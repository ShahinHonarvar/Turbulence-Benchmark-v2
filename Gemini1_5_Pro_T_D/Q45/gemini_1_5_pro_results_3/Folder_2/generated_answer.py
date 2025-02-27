import itertools
  from collections import Counter

def palindromes_between_indices(string):
    letters = ''.join((char for char in string[1:6] if char.isalpha())).lower()
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for combination in itertools.permutations(letters, length):
            word = ''.join(combination)
            if word == word[::-1] and word not in palindromes:
                if all((count <= Counter(letters)[char.lower()] for char, count in Counter(word).items())):
                    palindromes.add(word)
    return palindromes