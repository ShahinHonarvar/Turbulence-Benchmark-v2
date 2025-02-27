from itertools import product

def palindrome_of_length_n(word):
    low_word = word.lower()
    letters = set(low_word)
    palindromes = set()
    for substring in product(letters, repeat=40):
        if ''.join(substring) in low_word:
            palindromes.add(''.join(substring))
    return palindromes