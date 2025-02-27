def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    char_range = string[56:96]
    output = [char for char in char_range if '&' < char <= 'T' and char in vowels]
    return output