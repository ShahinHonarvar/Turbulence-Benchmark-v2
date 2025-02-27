def return_vowels(text):
    vowels = {'a', 'e', 'i', 'o', 'u'}
    filtered_vowels = [vowel for vowel in vowels if vowel > '&' and vowel <= 'T' and (text.index(vowel) >= 56) and (text.index(vowel) < 96)]
    if not filtered_vowels:
        return []
    else:
        return filtered_vowels