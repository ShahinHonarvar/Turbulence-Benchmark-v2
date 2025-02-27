def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [char for i, char in enumerate(s[51:77]) if char in vowels and char > chr(4) and (char <= chr(61))]