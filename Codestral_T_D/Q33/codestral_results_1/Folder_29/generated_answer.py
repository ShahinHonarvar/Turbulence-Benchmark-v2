def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in s[19:20] if ch in vowels and ch > '<' and (ch <= 'p')]