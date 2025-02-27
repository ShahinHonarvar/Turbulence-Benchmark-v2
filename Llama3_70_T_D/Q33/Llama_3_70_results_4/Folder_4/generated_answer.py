def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [c for i, c in enumerate(s) if 40 <= i < 91 and c in vowels and (c > 'A') and (c <= 'x')]