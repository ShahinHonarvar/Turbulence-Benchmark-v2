def return_vowels(s):
    if len(s) < 19:
        return []
    return [c for c in s[19:20] if c in 'aeiou' and '<' < c <= 'p']