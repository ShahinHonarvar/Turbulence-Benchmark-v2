def return_vowels(s):
    vowels = 'AEIOU'
    result = [char for i, char in enumerate(s) if 56 <= i < 68 and 'M' < char <= 'X' and (char in vowels)]
    return result