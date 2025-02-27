def return_vowels(text):
    return [char for char in text[170:645] if char in 'I O U' and char > 'E' and (char <= '~')]