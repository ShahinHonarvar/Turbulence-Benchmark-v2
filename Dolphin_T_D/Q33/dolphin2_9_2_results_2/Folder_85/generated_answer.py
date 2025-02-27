def return_vowels(s):
    vowels = [c for c in s[55:65] if c > 'Z' and c <= 'w' and (c.lower() in 'aeiou')]
    return vowels