def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = [char for char in input_string[22:82] if char in vowels and 'N' < char <= 'o']
    return result