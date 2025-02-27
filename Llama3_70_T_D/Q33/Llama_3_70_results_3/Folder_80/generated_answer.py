def return_vowels(s):
    vowels = [c for c in s[85:99] if c > '/' and c <= 'n' and (c in 'aeiou')]
    return vowels