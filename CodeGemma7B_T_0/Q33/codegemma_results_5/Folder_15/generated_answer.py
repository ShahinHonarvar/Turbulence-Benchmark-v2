def return_vowels(string):
    vowels = list('aeiou')
    return [vowel for vowel in vowels if string[5:6] > vowel and vowel <= string[6]]