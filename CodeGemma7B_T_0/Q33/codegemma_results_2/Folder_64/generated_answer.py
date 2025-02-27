def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [vowel for vowel in vowels if text.index(vowel) > 1 and text.index(vowel) < 7 and (vowel > 'F') and (vowel <= 'j')]