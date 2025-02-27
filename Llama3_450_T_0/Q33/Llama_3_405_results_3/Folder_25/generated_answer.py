def return_vowels(s):
    vowels = 'aeiou'
    return [char for i, char in enumerate(s) if 28 <= i < 76 and '+' < char <= 'z' and (char in vowels)]