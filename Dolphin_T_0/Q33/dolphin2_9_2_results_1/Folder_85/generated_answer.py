def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[55:65] if c in vowels and 'z' < c <= 'w']