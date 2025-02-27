def return_vowels(text):
    return [char for char in text[34:58] if char in 'aeiou' and char > 'b' and (char <= 'o')]