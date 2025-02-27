def return_vowels(s):
    return [c for c in s[47:61] if c in 'aeiouAEIOU' and ord(c) > 9 and (ord(c) <= ord('O'))]