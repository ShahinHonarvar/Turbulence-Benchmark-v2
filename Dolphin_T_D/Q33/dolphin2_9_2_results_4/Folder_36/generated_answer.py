def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    part_string = string[604:949]
    result = [char for char in part_string if char in vowels and char > 'n' and (char <= 'u')]
    return result