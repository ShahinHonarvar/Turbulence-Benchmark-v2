def return_vowels(s):
    return [c for c in s[71:88] if c in 'aeiouAEIOU' and ord(c) > 9 and (ord(c) <= ord('P'))]