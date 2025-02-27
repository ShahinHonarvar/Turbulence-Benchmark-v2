def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [vowel for vowel in string[837:975] if vowel in vowels and 'N' < vowel <= 'W']