def return_vowels(s):
    vowels = 'AEIOU'
    result = [c for c in s[260:322] if c in vowels and '%' < c <= 'U']
    return result