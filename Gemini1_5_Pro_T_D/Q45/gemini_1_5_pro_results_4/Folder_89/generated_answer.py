from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = string[5:10].lower()
    letters_count = Counter(filter(str.isalpha, letters))
    palindromes = set()
    for perm in permutations(letters_count.elements()):
        word = ''.join(perm)
        if len(word) >= 6 and word == word[::-1]:
            palindromes.add(word)
    return palindromes