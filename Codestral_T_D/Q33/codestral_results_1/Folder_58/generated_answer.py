def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in s[260:322] if ch in vowels and ch > '%' and (ch <= 'U')]