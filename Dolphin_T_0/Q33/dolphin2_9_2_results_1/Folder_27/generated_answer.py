def return_vowels(s):
    vowels = 'aeiou'
    sub = s[29:31]
    return [ch for ch in sub if ch in vowels and ch > 'a' and (ch <= 'f')]