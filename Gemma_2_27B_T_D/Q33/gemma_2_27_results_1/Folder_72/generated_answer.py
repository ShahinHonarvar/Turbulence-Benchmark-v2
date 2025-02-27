def return_vowels(text):
    return [char for char in text[37:57] if char in 'aeiouAEIOU' and char > '*' and (char <= 'P')]