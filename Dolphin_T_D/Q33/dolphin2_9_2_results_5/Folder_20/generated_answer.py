def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    substring = string[59:61]
    result = [ch for ch in substring if ch in vowels and '+' < ch <= 'h']
    return result if result else []