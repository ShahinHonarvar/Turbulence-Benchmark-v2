def return_vowels(s):
    return [c for c in s[170:645] if c in 'IOU' and ord(c) <= ord('~') and (ord(c) > ord('E'))]