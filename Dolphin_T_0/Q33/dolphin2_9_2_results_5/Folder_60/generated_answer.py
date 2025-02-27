def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[24:59] if 'n' < c.lower() <= 'u' and c.lower() in vowels]