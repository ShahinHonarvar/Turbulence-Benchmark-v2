def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    s = s[604:949]
    return [ch for ch in s if 'n' < ch <= 'u' and ch in vowels]