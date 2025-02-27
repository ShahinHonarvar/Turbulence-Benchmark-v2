def return_vowels(s):
    return [c for c in s[142:145] if c in 'aeiouAEIOU' and ord(c) > 4 and (ord(c) <= ord('o'))]