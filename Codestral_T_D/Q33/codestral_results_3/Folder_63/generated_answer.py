def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    substring = string[34:69]
    return [char for char in substring if char in vowels and char > '_' and (char <= 'o')]