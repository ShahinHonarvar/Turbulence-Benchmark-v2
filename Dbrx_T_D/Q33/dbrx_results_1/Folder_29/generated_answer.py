def return_vowels(input_string):
    vowels = [char for char in input_string[19:20] if 'a' <= char <= 'p' and char in 'aeiouAEIOU']
    return vowels