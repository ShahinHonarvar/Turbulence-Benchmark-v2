def return_vowels(s):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    return [c for c in s[32:97] if 'Q' < c <= ']' and c.lower() in vowels]