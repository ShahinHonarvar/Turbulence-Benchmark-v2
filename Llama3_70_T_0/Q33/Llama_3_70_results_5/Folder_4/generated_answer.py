def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[40:91] if c in vowels and c > 'A' and (c <= 'x')]