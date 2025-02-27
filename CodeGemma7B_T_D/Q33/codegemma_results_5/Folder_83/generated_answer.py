def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    result = [vowel for vowel in text[90:97] if vowel in vowels and vowel > '_' and (vowel <= 'x')]
    return result