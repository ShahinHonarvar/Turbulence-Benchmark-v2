def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [c for c in s[54:82] if c in vowels and c > '=' and (c <= '@')]
    return result