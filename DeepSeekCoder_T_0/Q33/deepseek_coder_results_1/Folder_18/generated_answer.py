def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [c for c in s[528:606] if c in vowels and 'M' < c <= 'X']
    return result