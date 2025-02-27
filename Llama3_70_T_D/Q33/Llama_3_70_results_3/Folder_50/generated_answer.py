def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [c for c in s[11:54] if c in vowels and '+' < c <= 'W']