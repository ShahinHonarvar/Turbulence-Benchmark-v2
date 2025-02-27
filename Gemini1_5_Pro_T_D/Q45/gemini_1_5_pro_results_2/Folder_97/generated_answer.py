from collections import Counter
  from itertools import permutations

def palindromes_between_indices(string):
    letters = set('abcdefghijklmnopqrstuvwxyz')
    relevant_characters = [string[i].lower() for i in range(5) if string[i].lower() in letters]
    palindromes = set()
    for length in range(3, len(relevant_characters) + 1):
        for candidate in permutations(relevant_characters, length):
            word = ''.join(candidate)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes