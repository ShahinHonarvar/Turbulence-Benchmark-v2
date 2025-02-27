def return_vowels(s):
    vowels = set('AEIOUaeiou')
    chars = list(s[837:975])
    return [c for c in chars if c in vowels and 'N' < c <= 'W']