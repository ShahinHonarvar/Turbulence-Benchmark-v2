def return_vowels(s):
    vowels = [c for c in s[13:37] if 'Z' < c <= '}' and c in 'AEIOU']
    return vowels