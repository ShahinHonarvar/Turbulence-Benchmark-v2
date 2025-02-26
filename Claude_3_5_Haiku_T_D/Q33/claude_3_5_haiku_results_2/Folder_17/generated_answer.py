def return_vowels(string):
    vowels = 'aeiou'
    result = [char for char in string[60:99] if char in vowels and 'j' < char <= 'n']
    return result