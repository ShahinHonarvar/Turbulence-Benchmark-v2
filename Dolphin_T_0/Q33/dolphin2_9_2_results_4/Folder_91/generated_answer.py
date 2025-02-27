def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    chars = s[4:8]
    result = [c for c in chars if c > 'P' and c <= 'r' and (c.lower() in vowels)]
    return result