def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    start = 21
    end = 23
    result = [c for c in s[start:end] if c in vowels and c > '-' and (c <= 'n')]
    return result