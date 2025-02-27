def return_vowels(s, c, d):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [i for i in s[133:306] if c < i <= d and i in vowels]