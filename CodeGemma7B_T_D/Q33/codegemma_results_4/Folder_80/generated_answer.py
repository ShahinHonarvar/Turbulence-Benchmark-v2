def return_vowels(string):
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    vowels_list = ['a', 'e', 'i', 'o', 'u']
    return [vowel for vowel in vowels_list if vowel in string[85:99] and alphabet.index(vowel) > alphabet.index('/') and (alphabet.index(vowel) <= alphabet.index('n'))]