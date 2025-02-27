def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [vowel for vowel in vowels if vowel in string and vowel > 'S' and (vowel <= 'U') and (string.index(vowel) >= 3) and (string.index(vowel) < 9)]