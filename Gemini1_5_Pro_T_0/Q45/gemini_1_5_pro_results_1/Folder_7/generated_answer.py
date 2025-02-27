import itertools
  from collections import Counter

def palindromes_between_indices(text):
    letters = ''.join(filter(str.isalpha, text[1:10])).lower()
    palindromes = set()
    for i in range(7, len(letters) + 1):
        for permutation in set(itertools.permutations(letters, i)):
            word = ''.join(permutation)
            if word == word[::-1] and word not in palindromes:
                if Counter(word) <= Counter(letters):
                    palindromes.add(word)
    return palindromes