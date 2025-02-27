def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [c for i, c in enumerate(s[528:606], 528) if c in vowels and 'M' < c <= 'X']