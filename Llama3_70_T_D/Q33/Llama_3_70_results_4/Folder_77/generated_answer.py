def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [c for i, c in enumerate(s[837:975]) if c in vowels and 'N' < c <= 'W']