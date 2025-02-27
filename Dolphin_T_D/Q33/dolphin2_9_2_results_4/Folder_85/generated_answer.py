def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[55:65] if c > 'Z' and c <= 'w' and (c in vowels)]