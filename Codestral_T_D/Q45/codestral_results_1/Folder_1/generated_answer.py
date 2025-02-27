from itertools import permutations

def palindromes_between_indices(string):
    letters = [char.lower() for char in string[4:8] if char.isalpha()]
    palindromes = set()
    for p in permutations(letters):
        word = ''.join(p)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    return palindromes