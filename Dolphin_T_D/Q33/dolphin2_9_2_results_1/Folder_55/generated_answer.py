def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [c for c in s[1:5] if c in vowels and '!' < c <= 'j']