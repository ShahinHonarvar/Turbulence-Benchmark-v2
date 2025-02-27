def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [c for c in s[4:8] if c in vowels and c > 'p' and (c <= 'r')]
    return result