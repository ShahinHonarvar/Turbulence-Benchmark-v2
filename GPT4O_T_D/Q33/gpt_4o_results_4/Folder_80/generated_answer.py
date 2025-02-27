def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    return [char for char in input_string[85:99] if char in vowels and '/' < char <= 'n']