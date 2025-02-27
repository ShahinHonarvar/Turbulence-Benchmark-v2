def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[47:61] if c in vowels and 9 < ord(c) <= ord('O')]