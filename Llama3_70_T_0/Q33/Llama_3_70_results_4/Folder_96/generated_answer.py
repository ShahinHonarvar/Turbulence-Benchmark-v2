def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [c for c in s[77:84] if c in vowels and c > '(' and (c <= 'G')]