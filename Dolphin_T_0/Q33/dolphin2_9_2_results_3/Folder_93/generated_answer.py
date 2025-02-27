def return_vowels(s):
    vowels = [c for c in s[54:82] if c > '&' and c <= '@' and (c.lower() in 'aeiou')]
    return vowels