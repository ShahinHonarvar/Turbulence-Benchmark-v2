from itertools import permutations

def palindromes_between_indices(string):
    letters = set(string[1:5].lower())
    english_letters = 'abcdefghijklmnopqrstuvwxyz'
    letters = set([letter for letter in letters if letter in english_letters])
    palindromes = set()
    for i in range(3, len(letters) + 1):
        for p in permutations(letters, i):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes