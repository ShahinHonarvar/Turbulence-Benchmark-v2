def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [c for c in s[37:57] if c in vowels and c > '*' and (c <= 'P')]