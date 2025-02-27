def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    substring = s[528:606]
    result = [c for c in substring if c in vowels and c > 'M' and (c <= 'X')]
    return result