def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in text[22:82] if char in vowels and 'N' < char <= 'o']