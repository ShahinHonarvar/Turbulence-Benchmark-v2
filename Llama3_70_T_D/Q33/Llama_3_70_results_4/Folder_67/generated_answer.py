def return_vowels(s):
    vowels = [c for c in s[21:59] if '/' < c <= 'a' and c in 'aeiou']
    return vowels