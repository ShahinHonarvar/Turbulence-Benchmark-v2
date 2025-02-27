def return_vowels(string):
    vowels = 'aeiou'
    char_range = string[21:59]
    result = [char for char in char_range if char in vowels and '/' < char <= 'a']
    return result