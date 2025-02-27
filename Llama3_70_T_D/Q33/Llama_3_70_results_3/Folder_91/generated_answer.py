def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for c in s[4:8] if c in vowels and c > 'P' and (c <= 'r')]