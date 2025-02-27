def return_vowels(s):
    vowels = 'aeiou'
    s = s[85:99]
    return [c for c in s if c in vowels and '/' < c and (c <= 'n')]