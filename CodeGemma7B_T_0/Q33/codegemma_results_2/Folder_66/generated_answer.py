def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [vowel for vowel in vowels if vowel in string and string.index(vowel) >= 63 and (string.index(vowel) < 79) and (vowel > 'D') and (vowel <= 'y')] or []