def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[5:7] if c in vowels and c > '\\x03' and (c <= '^')]