def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in set(s[14:60]) & set(filter(str.isalpha, vowels)) if 'D' < char <= 'v']