def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    return [char for char in input_string[8:10] if char in vowels and char > 'Y' and (char <= 's')]