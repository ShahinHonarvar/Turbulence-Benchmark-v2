def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in input_string[21:23] if char.lower() in vowels and char > '-' and (char <= 'n')]
    return result