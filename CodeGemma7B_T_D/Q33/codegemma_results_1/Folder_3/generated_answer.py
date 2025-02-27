def return_vowels(s):
    vowels = ['a', 'e', 'i', 'o', 'u']
    vocalized = [letter for letter in s.lower() if letter in vowels and s.index(letter) >= 50 and (s.index(letter) < 77) and (letter >= '#') and (letter <= 'r')]
    return vocalized if vocalized else []