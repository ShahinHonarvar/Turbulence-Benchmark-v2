def return_vowels(s):
    return [c for c in s[15:86] if c > '@' and c <= '~' and (c.lower() in 'aeiou')]