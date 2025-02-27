def return_vowels(s):
    return [c for c in s[13:35] if c in 'aeiouAEIOU' and ord(c) > 8 and (ord(c) <= 70)]