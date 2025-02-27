def return_vowels(s):
    vowels = [ch for ch in s[28:76] if ch > '+' and ch <= 'z' and (ch in 'aeiouAEIOU')]
    return vowels