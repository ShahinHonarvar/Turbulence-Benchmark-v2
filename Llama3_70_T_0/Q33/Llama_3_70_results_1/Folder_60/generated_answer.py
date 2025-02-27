def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [c for i, c in enumerate(s) if 24 <= i < 59 and c in vowels and ('N' < c <= 'U')]