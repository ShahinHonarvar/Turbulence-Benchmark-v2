def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[10:82] if c > '$' and c <= '@' and (c.lower() in vowels)]