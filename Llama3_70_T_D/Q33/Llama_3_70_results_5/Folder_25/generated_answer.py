def return_vowels(s):
    vowels = 'aeiou'
    return [c for i, c in enumerate(s[28:76]) if c in vowels and c > '+' and (c <= 'z')]