def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in text[11:61] if char in vowels and 'M' < char <= 'W']