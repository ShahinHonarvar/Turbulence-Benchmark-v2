import itertools
  from collections import Counter

def palindromes_between_indices(string):
    letters = 'abcdefghijklmnopqrstuvwxyz'
    filtered_string = ''.join((char for char in string[3:10] if char.lower() in letters))
    possible_palindromes = set()
    for i in range(5, len(filtered_string) + 1):
        for permutation in itertools.permutations(filtered_string, i):
            word = ''.join(permutation).lower()
            if word == word[::-1]:
                possible_palindromes.add(word)
    return possible_palindromes