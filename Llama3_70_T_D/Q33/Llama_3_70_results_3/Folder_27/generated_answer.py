def return_vowels(s):
    vowels = 'aeiou'
    return [c for i, c in enumerate(s) if 29 <= i < 31 and c in vowels and (c > 'a') and (c <= 'f')]