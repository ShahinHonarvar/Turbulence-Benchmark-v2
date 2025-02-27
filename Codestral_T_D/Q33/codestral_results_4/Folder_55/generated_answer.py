def return_vowels(s):
    return [c for c in s[1:5] if c > '!' and c <= 'j' and (c.lower() in 'aeiou')]