def return_vowels(s):
    vowels = 'AEIOU'
    return [c for i, c in enumerate(s[11:61], 11) if c in vowels and 'M' < c <= 'W']