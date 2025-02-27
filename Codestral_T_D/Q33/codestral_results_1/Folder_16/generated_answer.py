def return_vowels(s, c, d):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [ch for ch in s[133:306] if ch in vowels and c < ch <= d]