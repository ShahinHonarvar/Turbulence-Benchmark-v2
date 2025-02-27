def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[23:85] if c in vowels and 'W' < c <= 'v']