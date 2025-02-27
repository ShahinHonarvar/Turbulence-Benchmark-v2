def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    chars = s[23:38]
    return [ch for ch in chars if ch in vowels and ch > 'N' and (ch <= 'k')]