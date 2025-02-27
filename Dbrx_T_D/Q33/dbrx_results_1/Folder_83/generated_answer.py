def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [c for c in s if c in vowels and s.index(c) >= 90 and (s.index(c) < 97) and (c > 'a') and (c <= 'x')]
    return result