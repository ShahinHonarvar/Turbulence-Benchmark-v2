def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[20:43] if 5 < ord(c) < ord('M') and c.lower() in vowels]