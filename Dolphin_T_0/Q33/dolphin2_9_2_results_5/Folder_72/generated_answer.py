def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = [c for i, c in enumerate(s[37:57]) if c.lower() in vowels and '*' < c < 'P']
    return res