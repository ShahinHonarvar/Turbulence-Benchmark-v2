def return_vowels(s):
    vowels = 'aeiou'
    result = [c for i, c in enumerate(s) if 28 <= i < 76 and c in vowels and ('+' < c <= 'z')]
    return result