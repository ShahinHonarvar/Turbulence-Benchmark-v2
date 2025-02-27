def return_vowels(text):
    return [char for char in text[55:65] if char in 'aeiouAEIOU' and chr(ord('Z') + 1) <= char <= 'w']