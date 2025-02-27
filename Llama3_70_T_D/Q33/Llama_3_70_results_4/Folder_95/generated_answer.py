def return_vowels(s):
    vowels = [c for c in s[32:61] if 'A' < c <= 'P' and c in 'AEIOU']
    return vowels