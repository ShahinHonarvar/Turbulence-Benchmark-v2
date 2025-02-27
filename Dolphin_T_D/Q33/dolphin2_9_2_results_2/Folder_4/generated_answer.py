def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    chars = s[40:91]
    result = [c for c in chars if 'a' < c <= 'x' and c in vowels]
    return result