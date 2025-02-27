def return_vowels(s):
    vowels = 'aeiou'
    chars = s[202:872]
    res = [c for c in chars if 3 < ord(c) <= ord('>') and c in vowels]
    return res