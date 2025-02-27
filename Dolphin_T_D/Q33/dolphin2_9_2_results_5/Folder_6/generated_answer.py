def return_vowels(string):
    vowels = 'aeiou'
    vowels_in_range = [char for char in string[20:34] if char in vowels and char > 'U' and (char <= 'i')]
    return vowels_in_range