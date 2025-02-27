def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[77:84] if c in vowels and '(' < c <= 'G']