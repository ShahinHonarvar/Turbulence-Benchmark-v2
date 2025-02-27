def return_vowels(s):
    vowels = 'aeiou'
    chars = s[71:88]
    result = [c for c in chars if 9 < ord(c) <= ord('P') and c in vowels]
    return result