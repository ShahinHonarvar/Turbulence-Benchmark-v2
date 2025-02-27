def return_vowels(s):
    return [c for c in s[163:771] if c > ':' and c <= 'E' and (c.lower() in 'aeiou')]