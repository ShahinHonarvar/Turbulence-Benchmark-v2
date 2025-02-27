def return_vowels(s):
    vowels = 'AEIOUaeiou'
    result = [c for c in s[13:35] if c in vowels and ord(c) > ord(s[8]) and (ord(c) <= ord('F'))]
    return result