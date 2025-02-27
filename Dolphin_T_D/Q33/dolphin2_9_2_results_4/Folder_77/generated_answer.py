def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    chars = s[837:975]
    result = [c for c in chars if c > 'N' and c <= 'W' and (c in vowels)]
    return result