def return_vowels(s):
    vowels = [c for c in s[1:4] if 'C' < c.upper() <= 'I' and c.upper() in 'AEIOU']
    return vowels