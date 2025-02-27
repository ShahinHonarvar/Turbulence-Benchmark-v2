def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [c for i, c in enumerate(s[56:68]) if c in vowels and 'M' < c <= 'X']
    return result