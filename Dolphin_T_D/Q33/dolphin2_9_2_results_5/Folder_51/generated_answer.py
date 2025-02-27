def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    substring = s[55:67]
    res = [c for c in substring if c in vowels and 'm' < c <= 'x']
    return res