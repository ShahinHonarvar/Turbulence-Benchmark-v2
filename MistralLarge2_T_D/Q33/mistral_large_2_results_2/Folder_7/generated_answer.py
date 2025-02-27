def return_vowels(input_string):
    vowels = 'aeiouAEIOU'
    result = [char for char in input_string[202:872] if char in vowels and '3' < char <= '>']
    return result