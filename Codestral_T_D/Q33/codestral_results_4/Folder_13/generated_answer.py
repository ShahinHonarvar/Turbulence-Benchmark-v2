def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in s[149:313] if ch in vowels and 'M' < ch <= 'j']