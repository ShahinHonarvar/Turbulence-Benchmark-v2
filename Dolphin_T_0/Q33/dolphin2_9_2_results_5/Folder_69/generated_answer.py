def return_vowels(input_string):
    vowels = 'aeiou'
    interested_range = input_string[641:872]
    found_vowels = [char for char in interested_range if char.lower() in vowels and '>' < char <= 'q']
    return found_vowels