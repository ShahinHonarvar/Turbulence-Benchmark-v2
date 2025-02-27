def return_vowels(s):
    vowels = 'aeiou'
    chars = s[5:6]
    found = [c for c in chars if 3 < ord(c) <= ord('^') and c in vowels]
    return found