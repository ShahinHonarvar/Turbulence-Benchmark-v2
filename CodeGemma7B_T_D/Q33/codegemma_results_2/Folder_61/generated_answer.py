def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [vowel for vowel in vowels if text.index(vowel) >= 1 and text.index(vowel) < 4 and (vowel > 'C') and (vowel <= 'I')]
    return filtered_vowels if filtered_vowels else []