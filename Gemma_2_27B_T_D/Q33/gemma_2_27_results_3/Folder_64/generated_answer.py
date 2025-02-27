def return_vowels(s):
    return [c for c in s[1:7] if c in 'aeiouAEIOU' and ord(c) > ord('F') and (ord(c) <= ord('j'))]