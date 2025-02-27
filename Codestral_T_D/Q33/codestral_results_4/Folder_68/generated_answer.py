def return_vowels(s):
    return [c for c in s[1:9] if c > '?' and c <= 'k' and (c in 'aeiou')]