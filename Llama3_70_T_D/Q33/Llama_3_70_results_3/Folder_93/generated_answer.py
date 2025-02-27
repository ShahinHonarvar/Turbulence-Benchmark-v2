def return_vowels(s):
    vowels = 'aeiouAEIOU'
    return [c for i, c in enumerate(s[54:82]) if c > '=' and c <= '@' and (c in vowels)]