def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[24:59] if c in vowels and c > 'n' and (c <= 'u')]