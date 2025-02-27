def return_vowels(text):
    vowels = 'aeiouAEIOU'
    return [char for char in text[54:82] if char in vowels and '=' < char <= '@']