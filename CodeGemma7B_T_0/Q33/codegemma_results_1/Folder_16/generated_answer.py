def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [vowel for vowel in vowels if string[133:306].index(vowel) > string[133:306].index('c') and string[133:306].index(vowel) <= string[133:306].index('d')] or []