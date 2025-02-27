def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[20:41] if c.lower() in vowels and c.lower() > 'k' and (c.lower() <= 'z')]