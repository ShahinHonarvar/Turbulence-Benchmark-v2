def return_vowels(input_string):
    vowels = 'AEIOUaeiou'
    return [char for char in input_string[1:4] if char in vowels and 'C' < char <= 'I']