def return_vowels(string):
    vowels = 'aeiouAEIOU'
    filtered_vowels = [vowel for vowel in vowels if vowel > string[59] and vowel <= string[61]]
    return filtered_vowels