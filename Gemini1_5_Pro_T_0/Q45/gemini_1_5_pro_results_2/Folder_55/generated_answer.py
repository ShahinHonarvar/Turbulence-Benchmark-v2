from collections import Counter

def palindromes_between_indices(string):
    letters = set(string[0:3].lower()) & set('abcdefghijklmnopqrstuvwxyz')
    letters_count = Counter((char.lower() for char in string[0:3] if char.lower() in letters))
    palindromes = set()
    for letter in letters:
        if letters_count[letter] >= 3:
            palindromes.add(letter * 3)
        if letters_count[letter] >= 2:
            for other_letter in letters:
                if other_letter != letter and letters_count[other_letter] > 0:
                    palindromes.add(letter * 2 + other_letter)
                    palindromes.add(letter + other_letter + letter)
    return palindromes