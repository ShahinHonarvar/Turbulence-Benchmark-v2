def return_vowels(s):
    return [c for c in s[13:37] if c in 'aeiouAEIOU' and ord(c) > ord('Z') and (ord(c) <= ord('}'))]