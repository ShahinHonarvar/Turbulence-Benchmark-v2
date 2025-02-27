def return_vowels(s):
    return [c for c in s[20:43] if c in 'aeiouAEIOU' and ord(c) > 5 and (ord(c) <= ord('M'))]