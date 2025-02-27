def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in s[64:82] if ch > 'p' and ch <= 'z' and (ch in vowels)]