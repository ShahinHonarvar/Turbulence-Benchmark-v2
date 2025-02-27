def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[5:6] if c in vowels and 3 < ord(c) <= ord('^')]