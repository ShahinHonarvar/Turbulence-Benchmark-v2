def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in text[24:64] if char in vowels and 'F' < char <= 'h']