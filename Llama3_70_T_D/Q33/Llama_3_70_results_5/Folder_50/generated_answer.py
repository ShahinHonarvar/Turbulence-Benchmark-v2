def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [c for i, c in enumerate(s[11:54]) if c in vowels and '+' < c <= 'W']