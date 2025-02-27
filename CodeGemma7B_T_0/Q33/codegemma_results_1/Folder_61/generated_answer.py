def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [vowel for vowel in vowels if vowel in string and string.index(vowel) in range(1, 4) and (vowel > 'C') and (vowel <= 'I')]