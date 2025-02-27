def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    chars = s[56:90]
    result = [c for c in chars if 'k' < c <= 'z' and c in vowels]
    return result