def return_vowels(s):
    vowels = 'AEIOU'
    return [c for i, c in enumerate(s) if 56 <= i < 68 and c in vowels and ('M' < c <= 'X')]