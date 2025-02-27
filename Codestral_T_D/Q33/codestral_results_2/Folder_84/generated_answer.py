def return_vowels(input_string):
    vowels = 'aeiou'
    return [char for char in input_string[770:852] if char > 'B' and char <= 'i' and (char in vowels)]