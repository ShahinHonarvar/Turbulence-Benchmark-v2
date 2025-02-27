def return_vowels(string):
    return [char for char in string[528:606] if char in 'AEIOU' and char > 'M' and (char <= 'X')]