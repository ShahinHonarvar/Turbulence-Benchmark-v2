def return_vowels(s):
    vowels = 'aeiou'
    sub = s[82:90]
    return [c for c in sub if c > 'T' and c <= 'b' and (c in vowels)]