def return_vowels(input_string):
    vowels = 'AEIOUaeiou'
    return [char for char in input_string[10:97] if char in vowels and 'R' < char <= 'b']