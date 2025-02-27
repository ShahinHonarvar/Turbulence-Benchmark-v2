def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [ch for ch in s[1:7] if 'f' < ch <= 'j' and ch in vowels]
    return result