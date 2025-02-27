def return_vowels(s):
    return [c for c in s[2:7] if c in 'aeiou' and '^' < c <= 'd']