def return_vowels(s):
    vowels = [c for c in s[2:7] if c in 'aeiou' and '^' < c <= 'd']
    return vowels