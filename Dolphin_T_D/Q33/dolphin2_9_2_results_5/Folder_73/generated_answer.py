def return_vowels(s):
    vowels = 'aeiou'
    chars = s[47:89]
    return [c for c in chars if '@' < c <= 'n' and c in vowels]