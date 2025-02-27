def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    char_range = input_string[44:95]
    result = [char for char in char_range if 5 < ord(char) < ord('<') and char in vowels]
    return result