def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in text[20:34] if char in vowels and char > 'U' and (char <= 'i')]