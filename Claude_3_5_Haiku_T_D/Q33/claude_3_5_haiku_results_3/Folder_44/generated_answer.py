def return_vowels(input_string):
    vowels = 'aeiou'
    result = [char for char in input_string[46:49] if char in vowels and '[' < char <= 'p']
    return result