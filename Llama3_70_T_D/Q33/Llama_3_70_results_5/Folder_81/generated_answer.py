def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [c for i, c in enumerate(s) if 20 <= i < 43 and c in vowels and ('5' < c <= 'M')]