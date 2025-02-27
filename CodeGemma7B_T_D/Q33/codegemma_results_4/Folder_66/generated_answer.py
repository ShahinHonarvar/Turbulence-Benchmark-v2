def return_vowels(s):
    filtered_vowels = [c for c in s[63:79] if c.lower() in 'aeiou' and c.lower() > 'd' and (c.lower() <= 'y')]
    return filtered_vowels or []