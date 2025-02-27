def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[40:94] if 4 < ord(c) < ord('H') and c in vowels]