def return_vowels(s):
    vowels = 'AEIOU'
    result = [c for c in s[74:96] if c in vowels and 'I' < c <= 'X']
    return result