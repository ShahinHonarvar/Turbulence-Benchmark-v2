def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[837:975] if c.lower() in vowels and 'n' < c.lower() <= 'w']