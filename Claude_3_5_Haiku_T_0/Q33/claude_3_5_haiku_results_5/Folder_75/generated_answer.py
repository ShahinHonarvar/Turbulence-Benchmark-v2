def return_vowels(string):
    vowels = 'AEIOU'
    result = [char for char in string[20:41] if char in vowels and 'K' < char <= 'Z']
    return result