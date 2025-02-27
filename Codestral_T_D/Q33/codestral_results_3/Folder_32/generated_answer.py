def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in s[45:76] if 'b' < ch <= 'z' and ch in vowels]