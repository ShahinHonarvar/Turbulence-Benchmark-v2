def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [char for char in s[528:606] if char in vowels and 'M' < char <= 'X']
    return result