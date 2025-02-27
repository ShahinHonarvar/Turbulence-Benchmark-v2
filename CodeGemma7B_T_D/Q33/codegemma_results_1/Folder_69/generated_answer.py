def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [i for i in s if i in vowels and i > '>' and (i <= 'q')]