def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in s[23:57] if ch in vowels if 'a' <= ch <= 'd']