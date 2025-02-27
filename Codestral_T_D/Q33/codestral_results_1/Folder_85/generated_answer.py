def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in s[55:65] if ch > 'Z' and ch <= 'w' and (ch in vowels)]