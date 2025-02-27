def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [c for c in s[528:606] if c in vowels and 'M' < c <= 'X']