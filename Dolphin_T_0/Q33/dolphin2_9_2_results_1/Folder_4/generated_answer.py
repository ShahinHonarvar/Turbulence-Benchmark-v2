def return_vowels(s):
    vowels = [c for c in 'aeiou' if c > 'A' and c <= 'x']
    return [c for c in s[40:91] if c in vowels]