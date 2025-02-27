def return_vowels(s):
    vows = ['a', 'e', 'i', 'o', 'u']
    res = [c for c in s[142:145] if c in vows and 4 < ord(c) <= ord('o')]
    return res