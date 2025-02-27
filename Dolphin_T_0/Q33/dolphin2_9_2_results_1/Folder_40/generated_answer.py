def return_vowels(s):
    v = 'aeiou'
    return [c for c in s[2:7] if '^' < c <= 'd' and c in v]