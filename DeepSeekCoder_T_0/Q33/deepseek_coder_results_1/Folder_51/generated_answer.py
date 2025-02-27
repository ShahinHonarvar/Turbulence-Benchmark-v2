def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for char in s[56:68] if char in vowels and 'M' < char <= 'X']
    return result