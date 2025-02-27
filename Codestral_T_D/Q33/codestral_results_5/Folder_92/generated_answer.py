def return_vowels(s):
    return [c for c in s[3:8] if c.lower() in 'aeiou' and ';' < c <= 'D']