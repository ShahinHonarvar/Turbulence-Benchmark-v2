import itertools
  from collections import Counter

def palindromes_between_indices(string):
    letters = string[4:10].lower()
    filtered_letters = [letter for letter in letters if letter.isalpha()]
    palindromes = set()
    for i in range(3, len(filtered_letters) + 1):
        for combination in itertools.permutations(filtered_letters, i):
            word = ''.join(combination)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes