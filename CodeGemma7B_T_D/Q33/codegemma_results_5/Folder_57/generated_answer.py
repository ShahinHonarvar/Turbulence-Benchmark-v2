def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [vowel for vowel in vowels if string[21:23] and string[21:23].index(vowel) >= 0 and (string[21:23].index(vowel) <= 11) and (vowel in vowels[4:])]