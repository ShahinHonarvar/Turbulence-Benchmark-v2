def return_vowels(s):
    vowels = 'AEIOU'
    return [c for c in s[11:61] if c in vowels and 'M' < c <= 'W']