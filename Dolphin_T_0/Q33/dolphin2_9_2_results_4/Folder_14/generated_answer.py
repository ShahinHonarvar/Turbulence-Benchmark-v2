def return_vowels(s):
    return [c for c in s[47:61] if 9 < ord(c) <= ord('O') and c.lower() in 'aeiou']