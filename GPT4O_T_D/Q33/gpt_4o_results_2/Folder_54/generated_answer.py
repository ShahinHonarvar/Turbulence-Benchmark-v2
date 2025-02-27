def return_vowels(s):
    vowels = 'aeiou'
    return [ch for ch in s[23:85] if ch in vowels and 'W' < ch <= 'v']