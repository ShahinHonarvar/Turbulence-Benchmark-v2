def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in text[328:455] if char in vowels and char > '<' and (char <= 'z')]