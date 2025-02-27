def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    chars = s[19:20]
    result = [c for c in chars if c > '<' and c <= 'p' and (c in vowels)]
    return result