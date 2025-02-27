def return_vowels(str):
    vowels = 'aeiouAEIOU'
    filtered_vowels = [vowel for vowel in vowels if vowel > '@' and vowel <= 'n' and (47 <= ord(vowel) < 89)]
    return filtered_vowels