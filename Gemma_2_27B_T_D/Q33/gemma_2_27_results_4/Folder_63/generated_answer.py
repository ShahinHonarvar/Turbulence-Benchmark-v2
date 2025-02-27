def return_vowels(text):
    return [char for char in text[34:69] if char in 'aeiou' and char > '_' and (char <= 'o')]