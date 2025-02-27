def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [vowel for vowel in vowels if vowel > '=' and vowel <= '@' and (54 <= string.index(vowel) < 82)] or []