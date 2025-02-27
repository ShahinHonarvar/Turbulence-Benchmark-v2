def return_vowels(s):
    return [c for c in s[19:32] if c in 'aeiouAEIOU' and ord(c) > 0 and (ord(c) <= 7)]