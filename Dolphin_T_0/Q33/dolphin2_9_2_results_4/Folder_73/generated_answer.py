def return_vowels(s):
    vowels = [c for c in s[47:89] if c > '@' and c <= 'n' and (c in 'aeiou')]
    return vowels