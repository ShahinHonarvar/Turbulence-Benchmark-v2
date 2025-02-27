from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = Counter(string[1:9].lower())
    palindromes = set()
    for perm in permutations(''.join(letters.elements())):
        word = ''.join(perm)
        if len(word) >= 7 and word == word[::-1]:
            palindromes.add(word)
    return palindromes