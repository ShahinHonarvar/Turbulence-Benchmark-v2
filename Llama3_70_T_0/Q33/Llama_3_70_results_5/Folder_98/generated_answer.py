def return_vowels(s):
    vowels = 'AEIOU'
    return [c for c in s[3:9] if c in vowels and c > 'S' and (c <= 'U')]