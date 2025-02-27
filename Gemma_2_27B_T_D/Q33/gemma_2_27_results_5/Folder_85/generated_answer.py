def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[55:65] if c in vowels and c > 'Z' and (c <= 'w')]