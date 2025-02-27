from collections import Counter

def palindromes_between_indices(text):
    text = text.lower()
    letters = text[1:8]
    letters_count = Counter(filter(str.isalpha, letters))
    palindromes = set()
    for letter in letters_count:
        if letters_count[letter] >= 3:
            palindromes.add(letter * 3)
        if letters_count[letter] >= 2:
            for other_letter in letters_count:
                if other_letter != letter and letters_count[other_letter] >= 1:
                    palindromes.add(letter * 2 + other_letter)
                    palindromes.add(letter + other_letter + letter)
    return palindromes