def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [char for i, char in enumerate(s) if 24 <= i < 59 and char in vowels and ('N' < char <= 'U')]