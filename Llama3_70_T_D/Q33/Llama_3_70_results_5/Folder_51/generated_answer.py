def return_vowels(s):
    vowels = 'AEIOU'
    return [char for i, char in enumerate(s[56:68]) if char in vowels and 'M' < char <= 'X']