def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in s[40:91] if ch in vowels and 'A' < ch <= 'x']