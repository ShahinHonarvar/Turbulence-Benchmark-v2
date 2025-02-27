def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in s[27:57] if ch > 'o' and ch <= 'w' and (ch in vowels)]