def return_vowels(text):
    return [char for char in text[21:23] if char in 'aeiouAEIOU' and char > '-' and (char <= 'n')]