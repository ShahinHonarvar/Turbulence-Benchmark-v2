def return_vowels(s):
    vowels = [c for c in s[27:57] if c > 'o' and c <= 'w' and (c.lower() in 'aeiou')]
    return vowels