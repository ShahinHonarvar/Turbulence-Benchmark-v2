def return_vowels(string):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [vowel for vowel in vowels if vowel in string and vowel > '&' and (vowel <= 'T') and (string.index(vowel) >= 56) and (string.index(vowel) < 96)]
    return filtered_vowels or []