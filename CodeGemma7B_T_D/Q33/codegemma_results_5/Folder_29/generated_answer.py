def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    vowels_in_range = [vowel for vowel in vowels if text.index(vowel) in range(19, 20) and vowel > '<' and (vowel <= 'p')]
    return vowels_in_range