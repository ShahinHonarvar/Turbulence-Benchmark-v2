def return_vowels(s):
    vowels = 'AEIOU'
    s = s[20:41]
    return [c for c in s if c in vowels and c > 'K' and (c <= 'Z')]