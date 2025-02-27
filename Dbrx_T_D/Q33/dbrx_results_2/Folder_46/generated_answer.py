def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [char for char in set(s[10:83]) & set(vowels) if '%' < char <= 'e']