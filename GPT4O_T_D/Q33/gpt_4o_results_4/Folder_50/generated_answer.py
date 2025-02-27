def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    return [char for char in input_string[11:53] if char in vowels and '+' < char <= 'W']