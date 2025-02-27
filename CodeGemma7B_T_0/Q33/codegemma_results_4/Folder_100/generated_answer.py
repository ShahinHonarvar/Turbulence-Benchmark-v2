def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in text[23:75] if char in vowels and 'L' < char <= 'd']