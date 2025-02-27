def return_vowels(s):
    vowels = 'AEIOU'
    result = [char for i, char in enumerate(s) if 24 <= i < 59 and 'N' < char <= 'U' and (char in vowels)]
    return result