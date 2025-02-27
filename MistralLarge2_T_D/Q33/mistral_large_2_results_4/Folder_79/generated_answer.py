def return_vowels(input_string):
    vowels = {'A', 'E', 'I', 'O', 'U', 'a', 'e', 'i', 'o', 'u'}
    result = [char for char in input_string[74:96] if char in vowels and 'I' < char <= 'X']
    return result