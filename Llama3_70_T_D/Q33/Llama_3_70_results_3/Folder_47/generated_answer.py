def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[23:38] if c in vowels and c > 'N' and (c <= 'k')]