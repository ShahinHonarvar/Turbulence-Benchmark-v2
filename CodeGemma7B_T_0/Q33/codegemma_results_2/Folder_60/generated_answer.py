def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in text[24:59] if char in vowels and 'N' < char <= 'U']