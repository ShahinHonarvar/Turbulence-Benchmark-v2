def return_vowels(s):
    vowels = [c for c in s[14:60] if 'D' < c <= 'v' and c.lower() in 'aeiou']
    return vowels