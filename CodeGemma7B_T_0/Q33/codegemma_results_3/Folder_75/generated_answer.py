def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in text[20:41] if char in vowels and 'K' < char <= 'Z']