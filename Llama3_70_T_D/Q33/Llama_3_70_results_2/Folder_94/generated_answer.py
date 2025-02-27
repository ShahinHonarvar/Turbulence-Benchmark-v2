def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [c for c in s[40:94] if c in vowels and c > chr(4) and (c <= 'H')]