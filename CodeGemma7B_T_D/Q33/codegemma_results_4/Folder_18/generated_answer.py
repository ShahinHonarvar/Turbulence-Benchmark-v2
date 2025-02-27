def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
    filtered_vowels = [vowel for vowel in vowels if text.find(vowel) >= 528 and text.find(vowel) < 606 and (vowel > 'M') and (vowel <= 'X')]
    return filtered_vowels if filtered_vowels else []