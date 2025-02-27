from itertools import permutations

def palindromes_between_indices(string):
    letters = set(string[1:7].lower())
    letters = ''.join((letter for letter in letters if letter.isalpha()))
    palindromes = set()
    for length in range(6, len(letters) + 1):
        for p in permutations(letters, length):
            word = ''.join(p)
            if word == word[::-1]:
                palindromes.add(word)
    return palindromes