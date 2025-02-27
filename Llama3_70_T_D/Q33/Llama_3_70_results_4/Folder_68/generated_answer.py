def return_vowels(s):
    vowels = [c for c in s[1:9] if '?' < c <= 'k' and c in 'aeiou']
    return vowels