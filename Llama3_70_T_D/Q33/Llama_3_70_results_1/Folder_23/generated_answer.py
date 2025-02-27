def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [char for i, char in enumerate(s) if 56 <= i < 96 and '&' < char <= 'T' and (char in vowels)]