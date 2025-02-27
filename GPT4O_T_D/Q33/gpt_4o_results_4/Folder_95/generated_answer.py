def return_vowels(input_string):
    return [char for char in input_string[32:61] if 'A' <= char <= 'P' and char in 'AEIOU']