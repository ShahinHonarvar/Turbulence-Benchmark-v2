def return_vowels(s):
    vowels = 'AEIOU'
    return [c for i, c in enumerate(s) if 20 <= i < 41 and 'K' < c <= 'Z' and (c in vowels)]