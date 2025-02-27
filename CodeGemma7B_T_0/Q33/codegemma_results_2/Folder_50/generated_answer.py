def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [vowel for vowel in vowels if string.index(vowel) in range(11, 53) and vowel > string[10] and (vowel <= string[52])]