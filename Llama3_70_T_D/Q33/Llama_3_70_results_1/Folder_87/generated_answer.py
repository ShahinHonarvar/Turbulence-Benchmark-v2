def return_vowels(input_string):
    vowels = [char for char in input_string[34:58] if 'b' < char <= 'o' and char in 'aeiou']
    return vowels