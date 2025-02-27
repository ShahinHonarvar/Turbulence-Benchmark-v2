def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    substring = s[59:61]
    result = [ch for ch in substring if ch in vowels and '+' < ch <= 'h']
    return result