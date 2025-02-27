def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [vowel for vowel in vowels if vowel > 'N' and vowel <= 'W' and (text.lower().index(vowel) >= 837) and (text.lower().index(vowel) < 975)]
    return filtered_vowels if filtered_vowels else []