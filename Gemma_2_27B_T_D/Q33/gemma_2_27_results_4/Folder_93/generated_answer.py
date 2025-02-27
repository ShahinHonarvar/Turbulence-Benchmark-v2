def return_vowels(text):
    return [char for char in text[54:82] if char in 'aeiouAEIOU' and char > '=' and (char <= '@')]