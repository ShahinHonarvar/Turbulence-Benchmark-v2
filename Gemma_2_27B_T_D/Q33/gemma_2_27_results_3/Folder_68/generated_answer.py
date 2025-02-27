def return_vowels(s):
    return [c for c in s[1:9] if c in 'aeiou' and ord(c) > ord('?') and (ord(c) <= ord('k'))]