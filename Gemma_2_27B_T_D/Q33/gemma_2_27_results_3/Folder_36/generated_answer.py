def return_vowels(text):
    return [char for char in text[604:949] if char in 'AEIOU' and char > 'N' and (char <= 'U')]