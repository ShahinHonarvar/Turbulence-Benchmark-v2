def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [vowel for vowel in vowels if vowel > 'U' and vowel <= 'i' and (-20 <= str.index(vowel) < 34)]
    return filtered_vowels or []