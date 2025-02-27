def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in input_string[21:59] if char in vowels and char > '/' and (char <= 'a')]
    return result