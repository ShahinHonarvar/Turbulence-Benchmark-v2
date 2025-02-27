def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[64:82] if c > 'P' and c <= 'z' and (c in vowels)]