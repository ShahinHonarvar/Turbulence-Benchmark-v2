import re

def palindromes_between_indices(s: str) -> set:
    english_letters = re.compile('[a-zA-Z]')
    english_letters_in_range = english_letters.findall(s[4:9])
    palindromes = set()
    for letter in english_letters_in_range:
        if s[4:9].lower().count(letter.lower()) >= 3:
            palindromes.add(letter * 3)
        if s[4:9].lower().count(letter.lower()) >= 2 and s[4:9].lower().count(letter.lower()) <= 4:
            palindromes.add(letter * 2)
    return palindromes