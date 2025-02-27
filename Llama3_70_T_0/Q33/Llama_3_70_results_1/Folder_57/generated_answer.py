def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[21:24] if c in vowels and c > '-' and (c <= 'n')]