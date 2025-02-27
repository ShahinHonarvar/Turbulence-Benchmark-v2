from string import ascii_lowercase

def return_vowels(text):
    return [char for char in text[34:69] if char not in ascii_lowercase[:3] and char <= 'o']