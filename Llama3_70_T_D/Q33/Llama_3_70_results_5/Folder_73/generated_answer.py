def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[47:89] if c in vowels and c > '@' and (c <= 'n')]