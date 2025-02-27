def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    res = [ch for ch in s[23:75] if ch > 'L' and ch <= 'd' and (ch in vowels)]
    return res