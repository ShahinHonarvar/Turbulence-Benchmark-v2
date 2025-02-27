def return_vowels(s):
    return [c for c in s[10:82] if '$' < c <= '@' and c.lower() in 'aeiou']