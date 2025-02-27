def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [ch for ch in s[29:31] if ch in vowels and ch > 'a' and (ch <= 'f')]
    return result