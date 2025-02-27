def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    char_range = string[24:59]
    result = [char for char in char_range if char in vowels and char > 'n' and (char <= 'u')]
    return result