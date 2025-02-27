def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [char for i, char in enumerate(s) if i >= 11 and i < 61 and (char in vowels) and ('M' < char <= 'W')]