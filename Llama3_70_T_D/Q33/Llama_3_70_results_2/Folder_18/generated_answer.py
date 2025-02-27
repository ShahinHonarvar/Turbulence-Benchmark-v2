def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for i, char in enumerate(s) if 528 <= i < 606 and char in vowels and ('M' < char <= 'X')]
    return result