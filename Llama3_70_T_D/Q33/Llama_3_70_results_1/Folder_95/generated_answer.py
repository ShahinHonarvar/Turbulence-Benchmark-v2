def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[32:61] if c in vowels and c > '?' and (c <= 'P')]