def return_vowels(s):
    vowels = [c for c in s[5:7] if c in 'aeiouAEIOU' and c > '\\x03' and (c <= '^')]
    return vowels