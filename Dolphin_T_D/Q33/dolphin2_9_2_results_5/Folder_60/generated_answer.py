def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [v for v in s[24:59] if v in vowels and 'n' < v <= 'u']