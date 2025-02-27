def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in text[44:95] if char in vowels and char > '5' and (char <= '<')]