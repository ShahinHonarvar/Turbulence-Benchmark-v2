def return_vowels(s):
    vowels = 'aeiou'
    return [c for c in s[44:95] if 5 < ord(c) < ord('<') and c in vowels]