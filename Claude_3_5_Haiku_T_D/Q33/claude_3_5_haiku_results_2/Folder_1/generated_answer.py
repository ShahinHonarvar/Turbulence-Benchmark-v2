def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in text[24:64] if char.lower() in vowels and 'f' < char.lower() <= 'h']