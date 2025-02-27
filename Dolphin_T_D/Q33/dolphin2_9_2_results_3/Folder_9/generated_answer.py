def return_vowels(s):
    vowels = 'AEIOU'
    return [s[i] for i in range(13, 35) if c.isupper() and (ord(c) > ord('8') and c <= 'F') and (c in vowels)]