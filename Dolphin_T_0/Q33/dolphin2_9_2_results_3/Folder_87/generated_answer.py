def return_vowels(string):
    vowels = 'aeiou'
    vowels_in_range = [char for char in string[34:58] if char in vowels and 'b' < char <= 'o']
    return vowels_in_range