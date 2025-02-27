def return_vowels(s):
    return [c for c in s[71:88] if c > '9' and c <= 'P' and (c.lower() in 'aeiou')]