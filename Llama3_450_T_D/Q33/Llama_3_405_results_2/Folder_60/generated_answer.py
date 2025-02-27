def return_vowels(s):
    vowels = 'AEIOU'
    result = [c for i, c in enumerate(s[24:59]) if c in vowels and 'N' < c <= 'U']
    return result