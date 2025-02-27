def return_vowels(s):
    vowels = 'aeiou'
    chars = s[604:949]
    return [c for c in chars if 'n' < c <= 'u' and c in vowels]