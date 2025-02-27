def return_vowels(s):
    if len(s) < 261:
        return []
    return [c for c in s[260:322] if c in 'AEIOUaeiou' and '%' < c <= 'U']