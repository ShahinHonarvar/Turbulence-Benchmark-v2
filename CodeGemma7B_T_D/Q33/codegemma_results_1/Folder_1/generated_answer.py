def return_vowels(text):
    vowels = ['a', 'e', 'i', 'o', 'u']
    filtered_vowels = [vowel for vowel in vowels if vowel in text and text.index(vowel) >= 24 and (text.index(vowel) < 64) and (vowel > 'f') and (vowel <= 'h')]
    if not filtered_vowels:
        return []
    return filtered_vowels