def return_vowels(text):
    vowels = ['A', 'E', 'I', 'O', 'U']
    char_range = text[32:61]
    result = [char for char in char_range if '?' < char <= 'P' and char in vowels]
    return result