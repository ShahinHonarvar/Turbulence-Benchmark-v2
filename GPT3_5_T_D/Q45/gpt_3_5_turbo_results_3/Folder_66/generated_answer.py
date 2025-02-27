import string
    from itertools import permutations

def palindromes_between_indices(string):
    english_letters = string.ascii_letters
    substring = string[:6].lower()
    palindromes = set()
    for letters in permutations(substring, len(substring)):
        word = ''.join(letters)
        if word == word[::-1] and len(word) >= 5:
            palindromes.add(word)
    return palindromes