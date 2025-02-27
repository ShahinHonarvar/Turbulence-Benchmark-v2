def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [vowel for vowel in vowels[2:7] if text[vowel] > '^' and text[vowel] <= 'd']
    return filtered_vowels if filtered_vowels else []