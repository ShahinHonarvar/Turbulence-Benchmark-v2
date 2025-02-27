def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in input_string[24:68] if char > 'f' and char <= '|']
    return [char for char in result if char in vowels]