def return_vowels(s):
    return [c for c in s[528:606] if c > 'M' and c <= 'X' and (c.lower() in 'aeiou')]