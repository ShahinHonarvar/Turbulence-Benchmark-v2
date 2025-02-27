def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[45:76] if c in vowels and c > 'b' and (c <= 'z')]