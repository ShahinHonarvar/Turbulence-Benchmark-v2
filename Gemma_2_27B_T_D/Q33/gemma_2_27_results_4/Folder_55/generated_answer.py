def return_vowels(s):
    return [c for c in s[1:5] if c in 'aeiou' and ord(c) > ord('!') and (ord(c) <= ord('j'))]