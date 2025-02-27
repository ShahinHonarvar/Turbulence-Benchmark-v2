def return_vowels(text):
    vowels = list('aeiouAEIOU')
    selected_vowels = [vowel for vowel in vowels if vowel in text and vowels.index(vowel) >= 21 and (vowels.index(vowel) <= 23) and (vowel > '-') and (vowel <= 'n')]
    return selected_vowels