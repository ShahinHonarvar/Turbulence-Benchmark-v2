def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [vowel for vowel in vowels if vowel in string and string.index(vowel) >= 54 and (string.index(vowel) < 82) and (vowel >= '=') and (vowel <= '@')]