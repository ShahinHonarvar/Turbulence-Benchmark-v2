def return_vowels(s):
    vowels = 'AEIOU'
    return [c for c in s[20:41] if c in vowels and c > 'K' and (c <= 'Z')]