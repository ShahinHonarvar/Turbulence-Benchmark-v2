def return_vowels(string):
    vowels = string[46:49]
    new_vowels = [vowel for vowel in vowels if vowel > '[' and vowel <= 'p']
    return new_vowels if new_vowels else []