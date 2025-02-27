def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for i, char in enumerate(s) if 24 <= i < 59 and char in vowels and ('N' < char <= 'U')]
    return result