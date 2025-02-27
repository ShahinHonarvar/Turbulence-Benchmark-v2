def return_vowels(s):
    return [c for c in s[5:6] if c in 'aeiouAEIOU' and ord(c) > 3 and (ord(c) <= ord('^'))]