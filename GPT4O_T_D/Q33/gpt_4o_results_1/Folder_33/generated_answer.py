def return_vowels(input_string):
    vowels = 'AEIOUaeiou'
    result = [char for char in input_string[163:771] if char in vowels and ':' < char <= 'E']
    return result