def return_vowels(input_string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [char for char in input_string[1:9] if 'a' <= char <= 'k' and char in vowels]
    return result