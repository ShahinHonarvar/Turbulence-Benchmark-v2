def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in input_string[171:402] if char in vowels]