from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter(string[1:9].lower())
    keys = ''.join(letters.keys())
    palindromes = set()
    for i in range(7, len(keys) + 1):
        for p in permutations(keys, i):
            word = ''.join(p)
            if word == word[::-1] and all((letters[c] >= word.count(c) for c in word)):
                palindromes.add(word)
    return palindromes