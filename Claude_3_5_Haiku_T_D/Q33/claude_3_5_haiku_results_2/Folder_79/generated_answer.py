def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = [char for char in input_string[74:96] if char in vowels and 'I' < char <= 'X']
    return result