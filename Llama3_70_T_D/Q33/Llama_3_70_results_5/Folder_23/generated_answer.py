def return_vowels(s):
    vowels = [c for c in s[56:96] if c > '&' and c <= 'T' and (c in 'AEIOUaeiou')]
    return vowels