def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [char for i, char in enumerate(s) if 56 <= i < 68 and char in vowels and ('M' < char <= 'X')]