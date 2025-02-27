def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[23:85] if c in vowels and 'W' < c <= 'v']