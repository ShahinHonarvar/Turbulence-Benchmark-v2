from itertools import permutations

def palindromes_between_indices(s):
    English_letters = set('abcdefghijklmnopqrstuvwxyz')
    indices = range(4, 10)
    letters = [char.lower() for char in s if char.lower() in English_letters]
    palindromes = set()
    for p in permutations(letters, length=len(indices)):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 3:
            palindromes.add(word)
    return palindromes