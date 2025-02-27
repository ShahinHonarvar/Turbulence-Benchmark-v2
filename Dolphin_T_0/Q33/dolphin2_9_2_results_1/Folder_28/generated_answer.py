def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in input_string[41:50] if char > 'w' and char <= '[' and (char in vowels)]
    return result