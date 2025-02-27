def return_vowels(s):
    return [c for c in s[23:57] if c in 'aeiouAEIOU' and ord(c) > 0 and (ord(c) <= ord('d'))]