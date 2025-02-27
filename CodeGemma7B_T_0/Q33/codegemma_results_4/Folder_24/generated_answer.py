def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    return [vowel for vowel in vowels if text.index(vowel) >= 23 and text.index(vowel) < 57 and (text[text.index(vowel)] > '0') and (text[text.index(vowel)] <= 'd')]