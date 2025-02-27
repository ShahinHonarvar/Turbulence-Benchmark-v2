def return_vowels(s):
    vowels = 'aeiou'
    result = [ch for ch in s[47:61] if 9 < ord(ch) <= ord('O') and ch in vowels]
    return result