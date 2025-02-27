def return_vowels(s):
    vowels = 'AEIOU'
    result = [char for i, char in enumerate(s[24:59]) if char in vowels and 'N' < char <= 'U']
    return result