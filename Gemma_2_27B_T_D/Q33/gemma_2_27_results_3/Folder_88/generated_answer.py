def return_vowels(s):
    return [c for c in s[70:76] if c in 'aeiouAEIOU' and ord(c) > 2 and (ord(c) <= ord(':'))]