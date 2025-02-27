def return_vowels(string):
    vowels = 'aeiou'
    char_range = string[13:35]
    result = [char for char in char_range if 8 < ord(char) < ord('F') and char in vowels]
    return result