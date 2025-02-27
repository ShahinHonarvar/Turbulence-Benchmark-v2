def return_vowels(string):
    """Return a list of vowel English letters between index 37 and 57 (exclusive) that are greater than character * and smaller than or equal to character P."""
    vowels = [letter for letter in string if letter.lower() in 'aeiou' and index(letter) >= 37 and (index(letter) < 57) and (letter > '*') and (letter <= 'P')]
    return vowels