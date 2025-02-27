def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for i, char in enumerate(s) if 14 <= i < 60 and 'D' < char <= 'v' and (char in vowels)]
    return result