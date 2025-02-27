def return_vowels(s):
    return [c for c in s[69:82] if c in 'aeiouAEIOU' and ord(c) > ord('[') and (ord(c) <= ord('~'))]