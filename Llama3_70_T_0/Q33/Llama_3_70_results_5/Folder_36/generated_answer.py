def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [c for c in s[604:949] if c in vowels and 'N' < c <= 'U']