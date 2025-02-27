def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [char for i, char in enumerate(s) if 74 <= i < 96 and char in vowels and ('I' < char <= 'X')]