def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in vowels if text.index(char) in range(56, 96) and char > '&' and (char <= 'T')]