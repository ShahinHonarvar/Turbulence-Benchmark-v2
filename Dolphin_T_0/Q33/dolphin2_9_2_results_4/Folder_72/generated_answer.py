def return_vowels(string):
    vowels = 'aeiou'
    range_string = string[37:57]
    found_vowels = [char for char in range_string if char in vowels and char > '*' and (char <= 'P')]
    return found_vowels