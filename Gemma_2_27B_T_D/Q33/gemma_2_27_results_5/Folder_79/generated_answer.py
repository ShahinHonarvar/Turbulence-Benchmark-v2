def return_vowels(text):
    return [char for char in text[74:96] if char in 'AEIOUaeiou' and char > 'I' and (char <= 'X')]