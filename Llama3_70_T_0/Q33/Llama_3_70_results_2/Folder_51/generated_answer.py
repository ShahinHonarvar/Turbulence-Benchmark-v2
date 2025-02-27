def return_vowels(s):
    vowels = 'AEIOU'
    return [c for c in s[56:68] if c in vowels and c > 'M' and (c <= 'X')]