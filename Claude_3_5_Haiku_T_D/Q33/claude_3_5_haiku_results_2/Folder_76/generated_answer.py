def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = [char for char in input_string[495:837] if char in vowels and 'B' < char <= 't']
    return result