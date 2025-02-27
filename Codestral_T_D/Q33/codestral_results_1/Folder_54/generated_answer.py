def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    substring = string[23:85]
    result = [char for char in substring if char in vowels and char > 'W' and (char <= 'v')]
    return result