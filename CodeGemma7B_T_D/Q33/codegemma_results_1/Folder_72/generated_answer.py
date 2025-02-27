def return_vowels(string):
    vowels = list('aeiouAEIOU')
    filtered_vowels = [vowel for vowel in vowels if vowel in string and string.index(vowel) >= 37 and (string.index(vowel) < 57) and (vowel > '*') and (vowel <= 'P')]
    return filtered_vowels if filtered_vowels else []