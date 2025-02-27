def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in text[13:37] if char in vowels and char > 'Z' and (char <= 'z')]