def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [c for c in s[1:4] if c in vowels and 'C' < c <= 'I']