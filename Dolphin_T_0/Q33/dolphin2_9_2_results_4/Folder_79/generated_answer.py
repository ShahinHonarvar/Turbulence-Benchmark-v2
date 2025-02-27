def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in s[74:96] if ch > 'I' and ch <= 'X' and (ch in vowels)]