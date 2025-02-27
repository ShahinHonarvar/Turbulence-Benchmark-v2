def return_vowels(input_string):
    vowels = [char for char in input_string[3:9] if 'S' < char <= 'U' and char in 'AEIOUaeiou']
    return vowels