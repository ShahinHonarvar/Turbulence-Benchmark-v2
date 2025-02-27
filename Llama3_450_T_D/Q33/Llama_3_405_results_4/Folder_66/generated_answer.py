def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for i, char in enumerate(s) if 63 <= i < 79 and 'D' < char <= 'y' and (char in vowels)]
    return result