def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[14:60] if c.lower() in vowels and 'd' < c.lower() <= 'v']