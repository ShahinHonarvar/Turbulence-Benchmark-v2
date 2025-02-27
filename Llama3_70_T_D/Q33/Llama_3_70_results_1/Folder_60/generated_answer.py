def return_vowels(s):
    vowels = [c for c in s[24:60] if c.lower() in 'aeiou' and c > 'N' and (c <= 'U')]
    return vowels