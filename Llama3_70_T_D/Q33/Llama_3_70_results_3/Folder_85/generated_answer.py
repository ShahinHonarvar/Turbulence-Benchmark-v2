def return_vowels(s):
    vowels = 'AEIOUaeiou'
    return [c for c in s[56:65] if c in vowels and ord(c) > ord('Z') and (ord(c) <= ord('w'))]