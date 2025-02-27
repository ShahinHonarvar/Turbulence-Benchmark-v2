def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [c for c in s[71:88] if c in vowels and c > '9' and (c <= 'P')]