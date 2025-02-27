def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [c for i, c in enumerate(s) if 149 <= i < 313 and c in vowels and ('M' < c <= 'j')]