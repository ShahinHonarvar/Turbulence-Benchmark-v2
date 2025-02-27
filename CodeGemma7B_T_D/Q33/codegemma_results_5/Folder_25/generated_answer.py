def return_vowels(str):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [vowel for vowel in vowels if vowel in str and 28 <= str.index(vowel) < 76]
    filtered_vowels = [vowel for vowel in filtered_vowels if vowel > str[28] and vowel <= 'z']
    return filtered_vowels