def return_vowels(str):
    vowels = 'aeiouAEIOU'
    filtered_vowels = [vowel for vowel in vowels if vowel > 'N' and vowel <= 'o']
    return filtered_vowels