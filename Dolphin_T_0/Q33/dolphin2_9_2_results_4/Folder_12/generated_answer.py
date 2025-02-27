def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    res = [ch for ch in s[13:37] if ch > 'Z' and ch <= '}' and (ch in vowels)]
    return res