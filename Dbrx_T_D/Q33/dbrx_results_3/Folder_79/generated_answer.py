def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[74:96] if c.lower() in vowels and c > 'I' and (c <= 'X')]