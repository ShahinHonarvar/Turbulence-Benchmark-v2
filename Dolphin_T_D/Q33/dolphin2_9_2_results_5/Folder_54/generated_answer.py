def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [c for c in s[23:85] if c.lower() in vowels and c.lower() > 'w' and (c.lower() <= 'v')]
    return result