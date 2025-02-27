def return_vowels(s):
    return [c for c in s[44:95] if c in 'aeiouAEIOU' and ord(c) > 5 and (ord(c) <= ord('<'))]