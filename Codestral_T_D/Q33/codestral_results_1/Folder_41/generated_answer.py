def return_vowels(s):
    return [c for c in s[71:81] if c > '>' and c <= 'U' and (c.lower() in 'aeiou')]