def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in text[90:97] if char in vowels and char > '_' and (char <= 'x')]