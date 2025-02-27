def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [c for c in s[20:41] if c in vowels and 'K' < c <= 'Z']