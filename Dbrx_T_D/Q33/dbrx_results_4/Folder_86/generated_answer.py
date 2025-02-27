def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in input_string[273:275] if char.lower() in vowels and char > 'a' and (char <= 'o')]
    return result