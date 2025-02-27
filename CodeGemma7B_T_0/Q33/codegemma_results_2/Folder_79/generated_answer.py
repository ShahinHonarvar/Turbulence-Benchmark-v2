def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in text[74:96] if char in vowels and 'I' < char <= 'X']