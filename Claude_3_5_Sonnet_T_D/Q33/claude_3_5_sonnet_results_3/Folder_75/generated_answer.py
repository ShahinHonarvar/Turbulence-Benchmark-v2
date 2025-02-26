def return_vowels(s):
    vowels = 'AEIOU'
    return [c for c in s[20:41] if c.upper() in vowels and 'K' < c.upper() <= 'Z']